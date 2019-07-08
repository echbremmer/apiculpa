
import click
from flask import Flask 

from badapi import badapi

@click.command("start", short_help="Run a simple badapi")
@click.option(
    "--failrate", '-F',
    help='The chance that the API will not respond to a request. E.g. a value of 10 will result in the api having a 10% chance of not responding.', 
    type=int, 
    default=0
) 
@click.option(
    "--latency", '-L', 
    help='The number of seconds that the API will wait before sending a response.', 
    type=int, 
    default=0
)
@click.option(
    "--latency-range", '-R', 
    help='The given latency is randomly increased or decreased by the given amount.', 
    type=int, 
    default=0
)
@click.argument('input', type=click.File('r'))
def start_command(
    failrate, latency, latency_range, input
):

    """
    Starts a simple dummy API with configurable latency and reliability. Defaults to a reliable and fast API. Using the following options we can introduce following behaviour:
    """
    print('doing the flask thing now')
    
    #app = Flask(__name__)


    #@app.route('/')
    #def hello():
    #    return 'Hello, World!'

    #app.run(debug=True)   
    badapi.BadApi()
    #click.echo(badapi. something? , output)
    print('boem')


if __name__ == '__main__':
    start_command()
