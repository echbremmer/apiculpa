"""
    server.py
    ~~~~~~~~~
    This module implements the server. 
    
    :copyright: 2019 Emile Bremmer
    :license: MIT
"""

from .handler import APIHTTPRequestHandler

from http.server import HTTPServer


class APIServer:
    def __init__(self, behaviour, port, host):
        requesthandler = APIHTTPRequestHandler
        requesthandler.behaviour = behaviour

        print("*  ")
        print("* API available on " + str(host) + ":" + str(port))
        server = HTTPServer((host, port), requesthandler)
        server.serve_forever()

