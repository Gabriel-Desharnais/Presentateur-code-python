#!/usr/bin/python3
# coding: utf8
from threading import Thread
class LanceLeComServeur(Thread):
	def __init__(self):
		import socket
		Thread.__init__(self)
		self.TCP_IP = '127.0.0.1'
		self.TCP_PORT = 5005 # On devrait faire de quoi pour rendre ça transformable
		self.BUFFER_SIZE = 20  # Normally 1024, but we want fast response
		self.s=""
		self.s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((self.TCP_IP, self.TCP_PORT))
		self.s.listen(1)
		self.conn=""
		self.addr=""
		self.msg=""
	def servar(self):
		self.conn.close()
	def ex(self,st):
		try:
			a=open(st,'r')
			return a.read()
		except:
			return str(sys.exc_info())
	def lister(self):
		import os 
		l=os.listdir('presentemp/')
		del l[l.index("rap.html")]
		f=open('presentemp/rap.html','w')
		f.write("""<div id="content">\n<table style="width:100%">\n""")
		for i in l:
			f1=open("presentemp/"+i+ "/info.inf",'r')
			f.write("<tr>\n\t<th>"+f1.readline()+"</th>\n\t<th>"+f1.readline()+"</th>\n\t<th>"+f1.readline()+"</th>\n\t<th>"+f1.readline()+"</th>\n</tr>\n")
			f1.close()
		f.write("</table>\n</div>")
		f.close()
		return ""
	def creer(self,ls):
		import os
		l=ls.split('|')
		r=range(0,100)
		r=list(r)
		h=-1
		for f in r:
			if not os.path.exists('presentemp/'+str(f)):
				os.makedirs('presentemp/'+str(f))
				h=f
				break
		if not(h==-1):
			f=open('presentemp/'+str(h)+'/info.inf','w')
			for e in l:
				f.write(e+'\n')
			f.close()
		return "Creer"
	def servdem(self):
		self.msg=""
		self.conn, self.addr = self.s.accept()
		while 1:
			data = self.conn.recv(self.BUFFER_SIZE)
			self.msg+=str(data,'UTF-8')
			data
			if not data: break
			if bytes(chr(0),'UTF-8') in data: break
		self.msg=self.msg[0:self.msg.index("\x00")]
		if self.msg[0]=='o':
			self.conn.send(bytes(self.ex(self.msg[1:]),'UTF-8'))  # echo
			self.servar()
			return False
		elif self.msg[0]=='s':
			self.servar()
			return True
		elif self.msg[0]=='l':
			self.conn.send(bytes(self.lister(),'UTF-8'))  # echo
			self.servar()
			return False
		elif self.msg[0]=='e':
			self.conn.send(bytes(self.creer(self.msg[1:]),'UTF-8'))  # echo
			self.servar()
			return False
		else:
			self.servar()
			return True
	def run(self):
		while 1:
			if self.servdem():
				break