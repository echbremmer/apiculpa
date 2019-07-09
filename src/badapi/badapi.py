"""
    badapi.py
    ~~~~~~~~~
    This module implements the main application
    
    :copyright: 2019 Emile Bremmer
    :license: MIT
"""

from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

class BadApi:
    
    httpd = None

    def __init__(self, Port=3003, Latency=0, Reliability=100, Latency_range=0):
        
        self.httpd = HTTPServer(('localhost', Port), SimpleHTTPRequestHandler)
        print('Bad api started on localhost:' + str(Port))
        print('Latency: '+ str(Latency) + ' seconds')
        print('Raliability: '+ str(Reliability) + '%')
        print('To stop type: ctrl c ')
    
    def start(self):
        self.httpd.serve_forever()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!!!!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
