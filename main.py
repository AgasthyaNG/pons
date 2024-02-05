"""_summary_

    Returns:
        _type_: _description_
"""
import logging
from enum import Enum as enum
from kafka_io import kafka_source
from transformation.transformation import transform
from stdio1 import stdoutput

logging.basicConfig(level=logging.INFO)

class Source(enum):
    """
    Source of the data
    """
    KAFKA = 1
    PUBSUB = 2

class Destination(enum):
    """
    Destination of the message
    """
    STDIO = 1
    PUBSUB = 2

# if set to true the transformation will be performed
TRANSFORMATIONS = True

def run_application() -> None:
    """
    Run the application and log the start. Read data from a Kafka topic.

    Args:
        None

    Returns:
        None
    """
    logging.info("Starting the application")
    value = kafka_source.kafka_read_data({"bootstrap_servers": "localhost:9092"}, "kafka-topic")
    for msg in value:
        
        if TRANSFORMATIONS:
            results = transform(msg.value,"decodebase64","./transformation/custom/decodebase64.py")
        else:
            results = msg.value
        stdoutput.stdio(results)
if __name__ == '__main__':
    run_application()
