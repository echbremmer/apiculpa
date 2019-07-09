import click

from apiculpa.app import Apiculpa


@click.command("run", short_help="Run an apiculpa")
@click.option(
    "--failrate",
    "-F",
    help="The chance that the API will not respond to a request. E.g. a value of 10 will result in the api having a 10% chance of not responding.",
    type=int,
    default=50,
)
@click.option(
    "--latency",
    "-L",
    help="The number of seconds that the API will wait before sending a response.",
    type=int,
    default=6000,
)
@click.option(
    "--latency-range",
    "-R",
    help="The latency is randomly increased or decreased by the given amount.",
    type=int,
    default=2500,
)
@click.option(
    "--port", "-P", help="Port where the API will be listening", type=int, default=3002
)
@click.option("--host", "-H", help="Host of the API", default="localhost")
@click.argument("input", type=click.File("r"))
def run_command(failrate, latency, latency_range, port, host, input):

    """
    Starts a dummy API with configurable latency and failrate. Defaults to a pretty unreliable and slow API. Use these options to change its behaviour:
    """
    Apiculpa(input, latency, failrate, latency_range, host, port)