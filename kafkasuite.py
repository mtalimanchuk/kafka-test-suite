import click

import consumer
import producer


@click.group()
def cli():
    pass


@cli.command()
@click.option("-b", "--broker", help="Broker", required=True)
@click.option("-t", "--topic", help="Topic", required=True)
def consume(broker, topic):
    consumer.consume(broker, topic)


@cli.command()
@click.option("-b", "--broker", help="Broker", required=True)
@click.option("-t", "--topic", help="Topic", required=True)
@click.option("-f", "--file", help="Payload file", required=True)
def produce(broker, topic, file):
    producer.produce(broker, topic, file)


if __name__ == '__main__':
    cli()
