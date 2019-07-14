from time import sleep
from random import uniform
from random import randrange

from http.server import BaseHTTPRequestHandler

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

class Behaviour:
    def __init__(self, latency, failrate, latency_range, response_file):
        self.latency = latency
        self.failrate = failrate
        self.latency_range = latency_range

        self.content = str.encode(response_file.read())
        response_file.close()

