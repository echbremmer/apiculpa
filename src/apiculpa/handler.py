"""
    handler.py
    ~~~~~~~~~
    This module implements the handler for the API 
    
    :copyright: 2019 Emile Bremmer
    :license: MIT
"""

from time import sleep
from random import uniform
from random import randrange

from http.server import BaseHTTPRequestHandler


class APIHTTPRequestHandler(BaseHTTPRequestHandler):
    behaviour = dict()
    content = None

    def do_GET(self):
        random = randrange(0, 101, 2)
        if random < self.behaviour["failrate"]:
            # do nothing
            print("  Ignoring request")
            return
        else:
            if self.behaviour["latency"] != 0:
                # add additional latency based on latency-range if applicable
                if self.behaviour["latency_range"] == 0:
                    final_latency = self.behaviour["latency"]
                else:
                    final_latency = self.behaviour["latency"] + uniform(
                        0.0, self.behaviour["latency_range"]
                    )

                print("  Adding " + str(int(final_latency)) + " ms latency")
                sleep(final_latency / 1000)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("User-Agent", "apiculpa/BETA")
            self.send_header("x-latency-milliseconds", str(int(final_latency)))
            self.end_headers()
            self.wfile.write(str.encode(self.content))

            return
