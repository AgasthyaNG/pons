"""_summary_

    Returns:
        _type_: _description_
"""
import logging
from abc import ABC, abstractmethod
from kafka_io import kafka_source
from transformation.transformation import transform

logging.basicConfig(level=logging.INFO)

TRANSFORMATIONS = False

class Pons(ABC):
    """
        A description of the entire function, its parameters, and its return types.
    """

    @abstractmethod
    def source(self):
        """
        A description of the entire function, its parameters, and its return types.
        """
        pass

    @abstractmethod
    def transformation(self):
        """
        A description of the entire function, its parameters, and its return types.
        """
        pass

    @abstractmethod
    def destination(self):
        """
        A description of the entire function, its parameters, and its return types.
        """
        pass

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
        logging.info('Received message: %s', msg.value.decode('utf-8'))
        if TRANSFORMATIONS:
            print(transform(msg.value,"decodebase64","./transformation/custom/decodebase64.py"))
        else:
            print(msg)

if __name__ == '__main__':
    run_application()
