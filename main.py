import logging
from kafka_io import kafka_source
from typing import Dict

logging.basicConfig(level=logging.INFO)


def run_application() -> None:
    """
    Run the application and log the start. Read data from a Kafka topic.

    Args:
        None

    Returns:
        None
    """
    logging.info("Starting the application")
    kafka_source.kafka_read_data({"bootstrap_servers": "localhost:9092"}, "kafka-topic")
    
if __name__ == '__main__':
    run_application()