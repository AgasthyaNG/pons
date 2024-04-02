# This python package when used will publish messages to pubsub topic
# Requirments are that you have a pubsub service and GCP project set up
# And also the google pubsub client

import logging
from google.cloud import pubsub_v1
from google.auth import jwt


def callback(message):
    print(message.data)
    message.ack()


class ReadFromPubsub:
    """_summary_"""

    def __init__(self, project_id, topic_name, subscription) -> None:
        self.project_id = project_id
        self.topic_name = topic_name
        self.subscription = subscription

    def _topic_path(self) -> str:
        """_summary_

        Returns:
            _type_: str
        """
        return f"projects/{self.project_id}/topics/{self.topic_name}"

    def _subscription_path(self) -> str:
        """_summary_

        Returns:
            _type_: str
        """
        return f"projects/{self.project_id}/subscriptions/{self.subscription}"

    def consume(self):
        subscriber = pubsub_v1.SubscriberClient()
        topic_path = self._topic_path()
        sub_path = self._subscription_path()
        subscriber.create_subscription(name=sub_path, topic=topic_path)
        try:
            subscriber.subscribe(sub_path, callback=callback)
        except Exception as exe:
            raise ValueError(str(exe)) from exe
