# coding: utf8
"""----------------------------
C'est ce module qui contient les
 fonctions qui vont pouvoir rouler
le serveur web et faire l'interfaçage
entre elles et le les scripts cgi
------------------------------"""
from threading import Thread
class LanceLeServeur(Thread):
	httpd=""
	def __init__(self):
		Thread.__init__(self)
		global httpd
		import http.server
 
		PORT = 8888
		server_address = ("", PORT)

		server = http.server.HTTPServer
		handler = http.server.CGIHTTPRequestHandler
		handler.cgi_directories = ["/cgi"]

		httpd = server(server_address, handler)

	def run(self):
		httpd.serve_forever()

