"""
    badapi.py
    ~~~~~~~~~
    This module implements the main application. 
    
    Largely following approach discussed here:
    https://stackoverflow.com/questions/18444395/basehttprequesthandler-with-custom-instance
    
    todo: 
    -   right now the failrate results in a 'connection reset' as if the server
        simply doesn't respond anymore. It might be useful to instead give an 
        option to return a 500 instead. Maybe a 'failrate' and a '500rate'
    -   proper error handling
    
    :copyright: 2019 Emile Bremmer
    :license: MIT
"""
import time
#import random
from random import uniform
from random import randrange

from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

class Badness:
    def __init__(self, latency, failrate, latency_range):
        self.latency = latency
        self.failrate = failrate
        self.latency_range = latency_range

    def getLatency(self):
        return self.latency

    def getFailrate(self):
        return self.failrate
    
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
        # first determine whether to do something at all
        random = randrange(0, 101, 2)
        print('randomnumber ' + str(random))
        failrate = self.settings.getFailrate()
        print('failrate ' + str(failrate))

        if random  > self.settings.getFailrate():
            latency = self.settings.getLatency() / 1000
            range = self.settings.getLatency_range() / 1000
            
            if(range == 0):
                time.sleep(latency)
            else:
                totallatency = latency + uniform(0.0, range)
                #print('waiting this amount: ' + str(totallatency))
                time.sleep(totallatency)
            
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b'{}')
            return
        else:
            # Close the connection
            # SimpleHTTPRequestHandler inherits from BaseHTTPServer.BaseHTTPRequestHandler,
            # which in turn inherits from SocketServer.StreamRequestHandler
            #therefore we can simply do a self.connection.close()
            
            self.finish()
            self.connection.close()

class BadApi:
    def __init__(self, latency, failrate, latency_range):
        self.settings = Badness(latency, failrate, latency_range)
        
        print('>> Creating BadApi with following settings: ')
        print('>> Latency is: ' + str(self.settings.getLatency()) + ' milliseconds')
        print('>> Reliability: ' + str(self.settings.getFailrate()) + '% of calls will fail')
        print('>> Latency range is +/-: ' + str(self.settings.getLatency_range()) + ' milliseconds')

        self.server = http_server(self.settings)

#if __name__ == '__main__':
#    m = BadApi(3,5,1)