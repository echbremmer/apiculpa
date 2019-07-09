"""
    badapi.py
    ~~~~~~~~~
    This module implements the main application
    
    :copyright: 2019 Emile Bremmer
    :license: MIT
"""
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

class Badness:
    def __init__(self, latency, unreliability, latency_range):
        self.latency = latency
        self.unreliability = unreliability
        self.latency_range = latency_range

    def getLatency(self):
        return self.latency

    def getUnreliability(self):
        return self.unreliability
    
    def getLatency_range(self):
        return self.latency_range

class http_server:
    def __init__(self, settings):
        BadApiHandler.settings = settings
        print('>>  ')
        print('>> Server running on localhost:8080 ')
        server = HTTPServer(('localhost', 8080), BadApiHandler)
        server.serve_forever()

class BadApiHandler(BaseHTTPRequestHandler):
    settings = None
    def do_GET(self):
        time.sleep(self.settings.getLatency())
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b'{}')
        return

class BadApi:
    def __init__(self, latency, unreliability, latency_range):
        self.settings = Badness(latency, unreliability, latency_range)
        print('>> Creating BadApi with following settings: ')
        print('>> Latency is: ' + str(self.settings.getLatency()) + ' seconds')
        print('>> Reliability: ' + str(self.settings.getUnreliability()) + '% of calls will fail')
        print('>> Latency range is +/-: ' + str(self.settings.getLatency_range()) + ' seconds')

        self.server = http_server(self.settings)

if __name__ == '__main__':
    m = BadApi(3,5,1)