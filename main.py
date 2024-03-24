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
from argparse import ArgumentParser
from stdio1 import stdinput

# Set the logging level
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

parser = ArgumentParser()
parser.add_argument("--transformations", help="perform transformations", default=False)
parser.add_argument("--reqsource", help="source of the data queue", default=1)
parser.add_argument("--destinationq", help="destination of the data queue", default=1)
parser.add_argument("--project_id", help="project id", required=False)
parser.add_argument("--topic_name", help="topic name", required=False)
parser.add_argument("--service_account_info", help="service account info", required=False)
parser.add_argument("--topic", help="kafka topic", required=False)
parser.add_argument("--servers", help="kafka servers",required=False)
parser.add_argument("--transform_module", help="transformation module", required=False)
args = parser.parse_args() 
# Define the source and destination of the data
class Source(enum):
    """
    Source of the data
    """
    KAFKA = 1
    PUBSUB = 2
    STDIO = 3

class Destination(enum):
    """
    Destination of the message
    """
    STDIO = 1
    PUBSUB = 2


# if set to true the transformation will be performed
TRANSFORMATIONS = args.transformations
# The source of the data queue
REQSOURCE = int(args.reqsource)
# the destination of the data queue
DESTINATIONQ = int(args.destinationq)

# Pubsub configuration
PROJECT_ID = args.project_id
TOPIC_NAME = args.topic_name
SERVICE_ACCOUNT_INFO = args.service_account_info

# kafka configuration
TOPIC = args.topic
SERVERS = args.servers

TRANSFORM_MODULE = args.transform_module
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
            {"bootstrap_servers": SERVERS}, TOPIC
        )
        for msg in value:
            if TRANSFORMATIONS:
                results = transform(
                    msg.value, TRANSFORM_MODULE, f"./transformation/custom/{TRANSFORM_MODULE}.py"
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
    logging.info("Starting the application if it is not kafka source")
    if Source.STDIO.value == REQSOURCE:
        logging.info("Starting the std input listner")
        value = stdinput.stand_io()
        logging.info("The listner has stopped")
        logging.info(value )
        for msg in value:
            if TRANSFORMATIONS:
                results = transform(
                    msg, TRANSFORM_MODULE, f"./transformation/custom/{TRANSFORM_MODULE}.py"
                )
            else:
                results = msg
            if Destination.STDIO.value == DESTINATIONQ:
                stdoutput.stdio(results)
            else:
                logging.info("Sending message to pubsub")
                WriteToPubsub(
                    project_id=PROJECT_ID, topic_name=TOPIC_NAME, message=results
                ).publish()

if __name__ == "__main__":
    run_application()
