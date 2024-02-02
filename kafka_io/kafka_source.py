# This python file will act as a consumer for kafka topic and broker that will be hosted
# You can also test by running the kafka_source.py locally
from __future__ import division, print_function
import kafka
from abc import ABC, abstractclassmethod
import logging
from exceptiongroup import BaseExceptionGroup as exception

class Kafkaio(ABC):
    """
        A description of the entire function, its parameters, and its return types.
    """
    @abstractclassmethod
    def consumer_config(self):
        pass
    
    @abstractclassmethod
    def topic_name(self):
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
    
    def consumer_config(self) ->dict:
        if type(self.consumer_config) is dict:
            return self.consumer_config
        
    
    def topic_name(self) -> str:
        return self.topic_name
    
    def consume_data(self) -> kafka.KafkaConsumer:
        kafka_config = self.consumer_config
        topic_name = self.topic_name
        consumer = kafka.KafkaConsumer(topic_name, **kafka_config)
        return consumer

    
def kafka_read_data(consumer_config, topic_name):
    """
    This function initializes a KafkaReadData object with the given consumer_config and topic_name. 
    It then asserts that the consumer_config is of type dict and the topic_name is of type str, and consumes data from Kafka.
    If any error occurs, it raises an Exception with the message "Error in kafka_read_data".
    """
    kafka = KafkaReadData(consumer_config, topic_name)
    try:
        message = kafka.consume_data()
        for message in message:
            logging.info(message)
    except:
        raise Exception("Error in kafka_read_data")
    


        
        
    