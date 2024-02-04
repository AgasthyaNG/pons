"""_summary_

    Raises:
        Exception: that the consumer_config is not accessable or the topic_name is not accessable

    Returns:
        _type_: kafka messages
"""
from __future__ import division, print_function

from abc import ABC, abstractmethod
import logging
import kafka


class Kafkaio(ABC):
    """
        A description of the entire function, its parameters, and its return types.
    """

    @abstractmethod
    def consumer_config(self):
        """
        A description of the entire function, its parameters, and its return types.
        """
        pass

    @abstractmethod
    def topic_name(self):
        """
        A description of the entire function, its parameters, and its return types.
        """
        pass


class KafkaReadData(Kafkaio):
    """
            Initialize the object with the given consumer configuration and topic name.

            Args:
                consumer_config: The consumer configuration for the object.
                topic_name: The name of the topic for the object.

            Returns:
                None
    """

    def __init__(self, consumer_config, topic_name) -> None:
        self.consumer_config = consumer_config
        self.topic_name = topic_name

    def consumer_config(self) -> dict:
        """
        Return the consumer configuration as a dictionary if it is already a dictionary.
        """
        return self.consumer_config

    def topic_name(self) -> str:
        """
        Returns the topic name of the object.
        """
        return self.topic_name

    def consume_data(self) -> kafka.KafkaConsumer:
        """
        A method to consume data from Kafka and return a KafkaConsumer object.
        """
        kafka_config = self.consumer_config
        topic_name = self.topic_name
        consumer = kafka.KafkaConsumer(topic_name, **kafka_config)
        return consumer


def kafka_read_data(consumer_config, topic_name)-> kafka.KafkaConsumer:
    """
    This function initializes a KafkaReadData object with the given consumer_config and topic_name.
    It then asserts that the consumer_config is of type dict and the topic_name is of type str, and
    consumes data from Kafka.
    If any error occurs, it raises an Exception with the message "Error in kafka_read_data".
    """
    consumerism = KafkaReadData(consumer_config, topic_name)
    try:
        messages = consumerism.consume_data()
        return messages
    except Exception as exe:
        raise Exception(exe) from exe
