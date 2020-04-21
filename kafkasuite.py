import click

from commands import consumer, producer, administrator


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


@cli.command()
@click.option("-b", "--broker", help="Broker", required=True)
@click.option("-t", "--topic", required=True, help="New topic name")
@click.option(
    "-p",
    "--partitions",
    default=1,
    type=int,
    help="Number of partitions for the new topic (defaults to 1)",
)
@click.option(
    "--client", default="kafka-python-admin-client", help="Client ID",
)
def admin(broker, topic, partitions, client):
    administrator.create_topic(broker, topic, partitions, client)


if __name__ == "__main__":
    cli()
