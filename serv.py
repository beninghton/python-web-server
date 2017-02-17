#!/usr/bin/python3

#import SimpleHTTPServer
#import SocketServer

#PORT = 8000

#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#httpd = SocketServer.TCPServer(("", PORT), Handler)

#print ("serving at port", PORT)
#httpd.serve_forever()

from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
