#!/usr/bin/env python
# Kismet(new-core) XML parser 
Â
from xml.sax import make_parser
from xml.sax.handler import feature_namespaces
from xml.sax import saxutils
import sys

networkcount = 0
essidcount = 0
bssidcount = 0
falsecount = 0
truecount = 0
channel0 = 0
channel1 = 0
channel2 = 0
channel3 = 0
channel4 = 0
channel5 = 0
channel6 = 0
channel7 = 0
channel8 = 0
channel9 = 0
channel10= 0
channel11= 0
channel12= 0
channel13= 0
clientcount = 0

AESCCM=0
plain=0
PSK=0
TKIP=0
WEP=0
WPA=0

enclist = []

class ShowEncryption(saxutils.DefaultHandler):
	def __init__(self):
		self.network,self.crypto = 0,0
		self.hitme,self.hitme2,self.hitme3 = 0,0,0
		self.hitme4 = 0
		self.client = 0

	def startElement(self, name, attrs):
		global networkcount 
		global essidcount 
		global bssidcount 
		global falsecount
		global truecount
		global clientcount
		if name == 'wireless-client':
			clientcount+=1
		if name == 'wireless-network':
			infra = attrs.get('type')
			if infra == "infrastructure":
				print "------------"
				networkcount+=1
				self.network = 1
		if self.network == 1:
	        	if name == 'encryption':
				self.hitme = 1
			if name == 'essid':
				essidcount+=1
				cloak = attrs.get('cloaked')
				if cloak == 'true':
					truecount+=1
				else:
					falsecount+=1
				print "ESSID cloaking?" + cloak
				self.hitme2 = 1
			if name == 'BSSID':
				bssidcount+=1
				self.hitme3 = 1
			if name == 'channel':
				self.hitme4 = 1

	def characters(self,ch):
		global channel0
		global channel1
		global channel2
		global channel3
		global channel4
		global channel5
		global channel6
		global channel7
		global channel8
		global channel9
		global channel10
		global channel11
		global channel12
		global channel13
		global AESCCM
		global plain
		global PSK
		global TKIP
		global WEP
		global WPA
		global enclist
		if self.hitme == 1:
			self.crypto += 1
			print "Encryption:" + ch
			if ch == "AES-CCM":
				AESCCM+=1
			if ch == "None":
				plain+=1
			if ch == "PSK":
				PSK+=1
			if ch == "TKIP":
				TKIP+=1
			if ch == "WEP":
				WEP+=1
			if ch == "WPA":
				WPA+=1
			enclist.append(ch)
		if self.hitme2 == 1:
			print "ESSID:" + ch
		if self.hitme3 == 1:
			print "BSSID:" + ch
		if self.hitme4 == 1:
			if self.client == 0:
				print "Channel:" + ch
				self.client = 1
                                if ch == '0':    
                                        channel0+=1 
				if ch == '1':
					channel1+=1
                                if ch == '2':    
                                        channel2+=1 
                                if ch == '3':    
                                        channel3+=1 
                                if ch == '4':    
                                        channel4+=1 
                                if ch == '5':    
                                        channel5+=1 
                                if ch == '6':    
                                        channel6+=1 
                                if ch == '7':    
                                        channel7+=1 
                                if ch == '8':    
                                        channel8+=1 
                                if ch == '9':    
                                        channel9+=1 
                                if ch == '10':    
                                        channel10+=1 
                                if ch == '11':    
                                        channel11+=1 
                                if ch == '12':    
                                        channel12+=1 
                                if ch == '13':    
                                        channel13+=1 
	
	
 	def endElement(self, name):
		if self.network == 1:
			if name == "wireless-network":
				self.network = 0
                                # work out WEP only count
                                # work out WPA TKIP only count
                                # work out None only count
                                # work out WPA AES-CCM only count 
                                # work out WPA WPA TKIP AES-CCM (WPA1 & 2) count
                                # - add to counters
				global enclist
				print enclist 
				del enclist[:]
				print "Total encryptions supported: %d" % (self.crypto)
				self.crypto = 0
				self.client = 0
		self.hitme = 0 
		self.hitme2 = 0
		self.hitme3 = 0
		self.hitme4 = 0
	

if __name__ == '__main__':
	parser = make_parser()
	parser.setFeature(feature_namespaces, 0)
	dh = ShowEncryption()
    	parser.setContentHandler(dh)
	parser.parse(sys.argv[1])
	print "------------STATS-------------"
	print "NETWORKS: %d" % (networkcount)
	print "ESSIDS: %d" % (essidcount)
	print "CLOAKED: %d" % (truecount)
	print "UNCLOAKED: %d" % (falsecount)
	print "BSSIDS: %d" % (bssidcount)
	print "CHANNEL0: %d" % (channel0)
        print "CHANNEL1: %d" % (channel1)
        print "CHANNEL2: %d" % (channel2)
        print "CHANNEL3: %d" % (channel3)
        print "CHANNEL4: %d" % (channel4)
        print "CHANNEL5: %d" % (channel5)
        print "CHANNEL6: %d" % (channel6)	
        print "CHANNEL7: %d" % (channel7)
        print "CHANNEL8: %d" % (channel8)
        print "CHANNEL9: %d" % (channel9)
        print "CHANNEL10: %d" % (channel10)
        print "CHANNEL11: %d" % (channel11)
        print "CHANNEL12: %d" % (channel12)
        print "CHANNEL13: %d" % (channel13)
	print "CLIENTS: %d" % (clientcount)
	print "AES-CCM: %d" % (AESCCM)
	print "None: %d" % (plain)
	print "PSK: %d" % (PSK)
	print "TKIP: %d" % (TKIP)
	print "WEP: %d" % (WEP)
	print "WPA: %d" % (WPA)

