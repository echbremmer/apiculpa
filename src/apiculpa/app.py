"""
    app.py
    ~~~~~~~~~
    This module implements the main application. 
    
    todo: 
    -   failrate caused dropped connection; might be useful to also support return of 500 
        status codes.
    -   some error handling

    :copyright: 2019 Emile Bremmer
    :license: MIT
"""
from time import sleep
from random import uniform
from random import randrange

from twisted.web import server, resource
from twisted.internet import reactor, endpoints

from io import BytesIO


class Behaviour:
    def __init__(self, latency, failrate, latency_range):
        self.latency = latency
        self.failrate = failrate
        self.latency_range = latency_range


class API(resource.Resource):
    isLeaf = True
    numberRequests = 0
    behaviour = None
    reactor = None
    content = "{}"  # default

    def render_GET(self, request):
        self.numberRequests += 1

        random = randrange(0, 101, 2)
        if random < self.behaviour.failrate:
            # simulate server outtage
            print("  REQ RECEIVED: crashing server")
            self.reactor.crash()
            print("* Restarting ...")
            self.reactor.run()
            print("* Restarted")
            return
        else:
            print("  REQ RECEIVED: sending response")
            latency = self.behaviour.latency
            # latency = self.behaviour.getLatency()
            range = self.behaviour.latency_range()

            # if latency then sleep
            if latency == 0:
                latency_header = 0
            else:
                # add latency if applicable
                if range == 0:
                    final_latency = latency
                else:
                    final_latency = latency + uniform(0.0, range)

                latency_header = int(final_latency)
                print("  ADDING LATENCY ")
                sleep(final_latency / 1000)

            request.setHeader(b"Content-type", b"application/json")
            request.setHeader(b"User-Agent", b"Apiculpa/BETA")
            request.setHeader(
                b"x-latency-added-milliseconds", str.encode(str(latency_header))
            )

            return self.content.encode("ascii")


class App:
    def __init__(
        self, input, latency=0, failrate=0, latency_range=0, host="localhost", port=3002
    ):
        self.port = port
        self.host = host
        self.behaviour = Behaviour(latency, failrate, latency_range)

        maxlatency = latency + latency_range

        print("* Starting ...")
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

        APIsite = API()
        APIsite.behaviour = self.behaviour
        APIsite.content = input.read()

        endpoints.serverFromString(reactor, "tcp:" + str(self.port)).listen(
            server.Site(APIsite)
        )
        APIsite.reactor = reactor
        reactor.run()
