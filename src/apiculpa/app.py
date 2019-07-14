"""
    app.py
    ~~~~~~~~~
    This module implements the main application. 
      
    :copyright: 2019 Emile Bremmer
    :license: MIT
"""

from .server import APIServer


class App:
    def __init__(self, host, port, content, **kwargs):
        self.port = port
        self.host = host
        self.content = content
        self.behaviour = dict()

        for key in kwargs:
            self.behaviour[key] = kwargs[key]

        maxlatency = self.behaviour["latency"] + self.behaviour["latency_range"]

        print("* Starting API ")
        if self.behaviour["latency_range"] == 0:
            print(
                "* Added latency is " + str(self.behaviour["latency"]) + " milliseconds"
            )
        else:
            print(
                "* Added latency ranges from "
                + str(self.behaviour["latency"])
                + " to "
                + str(maxlatency)
                + " milliseconds"
            )

        print(
            "* Reliability: " + str(self.behaviour["failrate"]) + "% of calls will fail"
        )

        self.server = APIServer(self.port, self.host, self.behaviour, self.content)
