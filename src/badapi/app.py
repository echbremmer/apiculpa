"""
    badapi.py
    ~~~~~~~~~
    This module implements the main application. 
    
    Largely following approach discussed here:
    https://stackoverflow.com/questions/18444395/basehttprequesthandler-with-custom-instance
    
    todo: 
    -   right now the failrate results in a 'connection reset'. It 
        might be useful to instead give an option to return a 500 
        instead. Maybe a 'failrate' and a '500rate'?
    -   no headers are returned and data is hardcoded as an empty
        json.
    -   proper error handling
    -   print to console in case of purposeful fail or delay

    :copyright: 2019 Emile Bremmer
    :license: MIT
"""
from time import sleep 
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
    def __init__(self, settings, port, host):
        BadApiHandler.settings = settings
        print('*  ')
        print('* Server running on ' + str(host) + ':' + str(port))
        server = HTTPServer((host, port), BadApiHandler)
        server.serve_forever()

class BadApiHandler(BaseHTTPRequestHandler):
    settings = None
    def do_GET(self):
        random = randrange(0, 101, 2)    
        if random  < self.settings.getFailrate():
            # do nothing
            return
        else:
            latency = self.settings.getLatency() / 1000
            if (latency > 0):  
                range = self.settings.getLatency_range() / 1000
                
                if(range == 0):
                    sleep(latency)
                else:
                    totallatency = latency + uniform(0.0, range)
                    sleep(totallatency)
            
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b'{}')
            return

class BadApi:
    def __init__(self, latency=0, failrate=0, latency_range=0, host="localhost", port=3002):
        self.port = port
        self.host = host
        self.settings = Badness(latency, failrate, latency_range)
        
        maxlatency = latency + latency_range

        print('* Creating a bad api with following settings: ')
        if latency_range == 0:
            print('* Added latency is: ' + str(latency) + ' milliseconds')
        else:
            print('* Added latency ranges from: ' + str(latency) + ' to ' + str(maxlatency) + ' milliseconds')
        
        print('* Reliability: ' + str(self.settings.getFailrate()) + '% of calls will fail')

        self.server = http_server(self.settings, self.port, self.host)

#if __name__ == '__main__':
#    m = BadApi(3,5,1)