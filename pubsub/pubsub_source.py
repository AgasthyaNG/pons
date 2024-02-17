# This library will act as a consumer for pubsub subscription that is already
# reading message from a pubsub topic
# You can also test by running the pubsub_source.py locally to write to standard output

import logging
from google.cloud import pubsub_v1
from google.auth import jwt

audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

# Source pubsub topic 
class PubSubReadData:
    """
    Initialize the object with the given subscription name and project id.

    Args:
        subscription_name: The name of the subscription for the object.
        project_id: The project id for the object.

    Returns:
        None
    """
    def __init__(self, subscription_name, project_id, topic_name, service_account_info) -> None:
        self.subscription_name = subscription_name
        self.project_id = project_id
        self.topic_name = topic_name
        self.service_account_info = service_account_info
    def read_data(self):
        """
        A method to read data from pubsub and return a SubscriberClient object.
        """
        credentials = jwt.Credentials.from_service_account_info(
            service_account_info, audience=audience
        )
        subscriber = pubsub_v1.SubscriberClient(credentials = credentials)
        subscriber.create_subscription(
            name = self.subscription_name,
            topic = self.topic_name
        )
        return subscriber

def callback(message):
    print(message.data)
    message.ack()
    
def pubsub_read_data(subscription_name, project_id, topic_name, service_account_info) -> pubsub_v1.SubscriberClient:
    """
    This function initializes a PubSubReadData object with the given subscription_name and project_id.
    It then asserts that the subscription_name is of type str and the project_id is of type str, and
    reads data from pubsub.
    If any error occurs, it raises an Exception with the message "Error in pubsub_read_data".
    """
    
    subscribe = PubSubReadData(subscription_name, project_id, topic_name, service_account_info)
    subscriber = subscribe.subscribe(subscription_name, callback)
    print(f"Listening for messages on {subscription_name}...")
    
    try:    
        while True:
            pass
    except Exception as exe:
        raise Exception(exe) from exe

