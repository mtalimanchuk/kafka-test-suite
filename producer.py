from pathlib import Path
from time import sleep

from kafka import KafkaProducer


def _read_payload_from_file(path: str, encoding: str = "utf-8") -> bytes:
    path = Path(path)

    with path.open("r", encoding=encoding) as f:
        message = f.read()
    payload = bytes(message, encoding=encoding)
    return payload


def produce(broker: str, topic: str, path: str, repeat: int = 1, delay: int = 1) -> None:
    producer = KafkaProducer(
        bootstrap_servers=broker,
        value_serializer=None,
    )

    for n in range(repeat):
        payload = _read_payload_from_file(path)
        producer.send(topic, value=payload)
        print(f"Sending payload:\n{payload}")
        sleep(delay)
