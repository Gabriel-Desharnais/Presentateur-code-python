import socket
def mysend(s, msg):
	totalsent = 0
	while totalsent < len(msg):
		sent = s.send(bytes(msg[totalsent:],'UTF-8'))
		if sent == 0:
			raise RuntimeError("socket connection broken")
		totalsent = totalsent + sent
	s.send(bytes(chr(0),'UTF-8'))
def a(MESSAGE):
	global data
	TCP_IP = '127.0.0.1'
	TCP_PORT = 5006
	BUFFER_SIZE = 1024*1024

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	mysend(s,MESSAGE)
	data = s.recv(BUFFER_SIZE)
	s.close()
def gogogadjet(mes):
	a('o'+mes)
	return str(data,'UTF-8')
def gogocre(nom,cible,description,date):
	a('e'+nom+'|'+cible+'|'+description+'|'+str(date))
if __name__=='__main__':
	data=""
	a("""oaccueil.css""")
	print("received data:", data)