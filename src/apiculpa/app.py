"""
    app.py
    ~~~~~~~~~
    This module implements the main application. 
    
    Largely following approach discussed here:
    https://stackoverflow.com/questions/18444395/basehttprequesthandler-with-custom-instance
    
    todo: 
    -   right now the failrate results in a 'connection reset'. It 
        might be useful to instead give an option to return a 500 
        instead. Maybe a 'failrate' and a '500rate'?
    -   proper error handling

    :copyright: 2019 Emile Bremmer
    :license: MIT
"""
from time import sleep
from random import uniform
from random import randrange
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


class Behaviour:
    def __init__(self, latency, failrate, latency_range, response_file):
        self.latency = latency
        self.failrate = failrate
        self.latency_range = latency_range
        self.response_file = response_file

    def getLatency(self):
        return self.latency

    def getFailrate(self):
        return self.failrate

    def getLatency_range(self):
        return self.latency_range

    def getResponseFile(self):
        return self.response_file


class http_server:
    def __init__(self, behaviour, port, host):
        ApiCulpaHTTPRequestHandler.behaviour = behaviour
        print("*  ")
        print("* API available on " + str(host) + ":" + str(port))
        server = HTTPServer((host, port), ApiCulpaHTTPRequestHandler)
        server.serve_forever()


class ApiCulpaHTTPRequestHandler(BaseHTTPRequestHandler):
    behaviour = None

    def do_GET(self):
        random = randrange(0, 101, 2)
        if random < self.behaviour.getFailrate():
            # do nothing
            return
        else:
            latency = self.behaviour.getLatency()

            range = self.behaviour.getLatency_range()

            if range == 0:
                sleep(latency / 1000)
                latency_header = int(latency)
            else:
                totallatency = latency + uniform(0.0, range)
                sleep(totallatency / 1000)
                latency_header = int(totallatency)

            file = self.behaviour.getResponseFile()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("User-Agent", "Apiculpa/BETA")
            self.send_header("x-latency-milliseconds", str(latency_header))
            self.end_headers()
            self.wfile.write(str.encode(file.read()))

            return


class Apiculpa:
    def __init__(
        self, input, latency=0, failrate=0, latency_range=0, host="localhost", port=3002
    ):
        self.port = port
        self.host = host
        self.behaviour = Behaviour(latency, failrate, latency_range, input)

        maxlatency = latency + latency_range

        print("* Starting Apiculpa ")
        if latency_range == 0:
            print("* Added latency is " + str(latency) + " milliseconds")
        else:
            print(
                "* Added latency ranges from "
                + str(latency)
                + " to "
                + str(maxlatency)
                + " milliseconds"
            )

        print(
            "* Reliability: "
            + str(self.behaviour.getFailrate())
            + "% of calls will fail"
        )

        self.server = http_server(self.behaviour, self.port, self.host)
