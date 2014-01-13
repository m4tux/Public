#!/usr/bin/env python
#Draws a Sierpinski Triangle to a user supplied depth on command-line
#using a recursive function. This is not the best way of doing it.
#run with depth of recursion as arguement (e.g. ./sierpinski.py 4).
#Uses python clutter bindings (sudo apt-get install python-clutter).
import gobject, clutter, random, sys
from clutter import cogl

class Triangle(clutter.Actor):
	def __init__(self):
		clutter.Actor.__init__(self)
		self._color = clutter.Color(255,255,255,255)

	def set_color(self,a,b,c,d):
		self._color = clutter.Color(a,b,c,d)

	def do_paint(self):
		(x1,y1,x2,y2) = self.get_allocation_box()
		width=x2-x1
		height=y2-y1
		cogl.path_move_to(width / 2,0)
		cogl.path_line_to(width, height)
		cogl.path_line_to(0,height)
		cogl.path_line_to(width / 2, 0)
		cogl.path_close()
		cogl.set_source_color(self._color)
		cogl.path_fill()

def Sierpinski(size,x,y,depth):
	depth-=1
	color = random.randint(0,255)
        t1=Triangle()
        t1.set_size(size/2,size/2)     
        t1.set_position(x+(size/4),y)       
        t1.set_color(color,color,color,color)
        stage.add(t1)
	if depth != 0:
		Sierpinski(size/2,x+(size/4),y,depth)
        t2=Triangle()
        t2.set_size(size/2,size/2)    
        t2.set_position(x,y+(size/2))       
        t2.set_color(color,color,color,color)
        stage.add(t2)
	if depth != 0:
		Sierpinski(size/2,x,y+(size/2),depth)

        t3=Triangle()
        t3.set_size(size/2,size/2)       
        t3.set_position(x+(size/2),y+(size/2))    
        t3.set_color(color,color,color,color)
        stage.add(t3)
	if depth != 0:
		Sierpinski(size/2,x+(size/2),y+(size/2),depth)
	return 

if __name__ == "__main__":
	depth = int(sys.argv[1])
	gobject.type_register(Triangle)
	stage=clutter.Stage()
	stage.set_size(480,480)
	stage.set_color(clutter.Color(0,0,0,255))
	stage.connect('destroy',clutter.main_quit)
	(x,y) = (10,0)
	size = 440
	text = clutter.Text()
	text.set_text("Sierpinski Triangle")
	text.set_color((255,255,255,255))
	text.set_position(10,450)
	stage.add(text)
	Sierpinski(size,x,y,depth) 
	stage.show()
	stage.set_title("www.hackerfantastic.com")
	clutter.main()

