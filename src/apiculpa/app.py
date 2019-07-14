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

from .server import APIServer


class App:
    def __init__(self, host, port, content, **kwargs):
        self.port = port
        self.host = host
        self.content = content
        self.behaviour = dict()

        for key in kwargs:
            print("adding key: " + key + " with value: ")
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

        # self.server = APIServer(self.port, self.host, latency=10, latency_range=10, failrate=100, content=self.content)
        self.server = APIServer(self.port, self.host, self.behaviour, self.content)
