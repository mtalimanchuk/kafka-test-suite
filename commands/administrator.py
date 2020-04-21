from kafka import KafkaAdminClient
from kafka.admin import NewTopic


def create_topic(broker, topic, partitions, client):
    admin = KafkaAdminClient(bootstrap_servers=broker, client_id=client)

    topic = NewTopic(topic, num_partitions=partitions, replication_factor=2)

    admin.create_topics([topic])
