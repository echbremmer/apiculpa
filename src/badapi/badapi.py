"""
    badapi.py
    ~~~~~~~~~
    This module implements the main application
    
    :copyright: 2019 Emile Bremmer
    :license: MIT
"""

from flask import Flask

class BadApi:
    
    def __init__(self):

        app = Flask(__name__)

        @app.route('/')
        def hello():
            return 'Hello, World!'

        app.run(debug=False)   

