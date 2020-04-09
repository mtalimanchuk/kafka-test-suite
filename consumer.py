from kafka import KafkaConsumer

from config import TOPIC, BOOTSTRAP_SERVERS, GROUP_ID, SECURITY_PROTOCOL


def consume(broker, topic):
    consumer = KafkaConsumer(
        topic,
        auto_commit_interval_ms=1000,
        auto_offset_reset="earliest",
        bootstrap_servers=broker,
        enable_auto_commit=True,
    )

    for message in consumer:
        print(message)
