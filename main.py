"""_summary_

    Returns:
        _type_: _description_
"""

import logging
from enum import Enum as enum
from kafka_io import kafka_source
from transformation.transformation import transform
from stdio1 import stdoutput
from pubsub.pubsub_destination import WriteToPubsub

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
TRANSFORMATIONS = False
# The source of the data queue
REQSOURCE = 1
# the destination of the data queue
DESTINATIONQ = 0

PROJECT_ID = "robotic-augury-333723"
TOPIC_NAME = "test"
SERVICE_ACCOUNT_INFO = "service-account-info"


def run_application() -> None:
    """
    Run the application and log the start. Read data from a Kafka topic.

    Args:
        None

    Returns:
        None
    """

    logging.info("Starting the application")
    if Source.KAFKA.value == REQSOURCE:
        value = kafka_source.kafka_read_data(
            {"bootstrap_servers": "localhost:9092"}, "kafka-topic"
        )
        for msg in value:
            if TRANSFORMATIONS:
                results = transform(
                    msg.value, "decodebase64", "./transformation/custom/decodebase64.py"
                )
            else:
                results = msg.value
            logging.info("Message: %s transformed to %s", msg.value, results)
            if Destination.STDIO.value == DESTINATIONQ:
                stdoutput.stdio(results)
            else:
                logging.info("Sending message to pubsub")
                WriteToPubsub(
                    project_id=PROJECT_ID, topic_name=TOPIC_NAME, message=results
                ).publish()


if __name__ == "__main__":
    run_application()
