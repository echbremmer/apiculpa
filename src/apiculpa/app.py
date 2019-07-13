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

        self.content = str.encode(response_file.read())
        response_file.close()


class http_server:
    def __init__(self, behaviour, port, host):
        APIHTTPRequestHandler.behaviour = behaviour
        print("*  ")
        print("* API available on " + str(host) + ":" + str(port))
        server = HTTPServer((host, port), APIHTTPRequestHandler)
        server.serve_forever()


class APIHTTPRequestHandler(BaseHTTPRequestHandler):
    behaviour = None

    def do_GET(self):
        random = randrange(0, 101, 2)
        if random < self.behaviour.failrate:
            # do nothing
            print("  IGNORING REQUEST ")
            return
        else:
            if self.behaviour.latency == 0:
                latency_header = 0
            else:
                # add additional latency based on latency-range if applicable
                if self.behaviour.latency_range == 0:
                    final_latency = self.behaviour.latency
                else:
                    final_latency = self.behaviour.latency + uniform(0.0, self.behaviour.latency_range)

                latency_header = int(final_latency)
                print("  ADDING LATENCY ")
                sleep(final_latency / 1000)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("User-Agent", "apiculpa/BETA")
            self.send_header("x-latency-milliseconds", str(latency_header))
            self.end_headers()
            self.wfile.write(self.behaviour.content)

            return


class App:
    def __init__(
        self, input, latency=0, failrate=0, latency_range=0, host="localhost", port=3002
    ):
        self.port = port
        self.host = host
        self.behaviour = Behaviour(latency, failrate, latency_range, input)

        maxlatency = latency + latency_range

        print("* Starting API ")
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

        print("* Reliability: " + str(self.behaviour.failrate) + "% of calls will fail")

        self.server = http_server(self.behaviour, self.port, self.host)
