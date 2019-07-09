"""
    badapi.py
    ~~~~~~~~~
    This module implements the main application
    
    :copyright: 2019 Emile Bremmer
    :license: MIT
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import badapirequesthandler
from io import BytesIO

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


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
print('Server started on localhost:8000')
httpd.serve_forever()