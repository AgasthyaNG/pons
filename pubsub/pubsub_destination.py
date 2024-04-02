# This python package when used will publish messages to pubsub topic
# Requirments are that you have a pubsub service and GCP project set up
# And also the google pubsub client

import logging
from google.cloud import pubsub_v1
from google.auth import jwt


class WriteToPubsub:
    """_summary_"""

    def __init__(self, project_id, topic_name, message) -> None:
        self.project_id = project_id
        self.topic_name = topic_name
        self.message = message

    def _topic_path(self) -> str:
        """_summary_

        Returns:
            _type_: str
        """
        return f"projects/{self.project_id}/topics/{self.topic_name}"

    def publish(self):
        publisher = pubsub_v1.PublisherClient()
        topic_path = self._topic_path()
        try:
            publisher.publish(topic_path, self.message)
            logging.info("Message published to %s", self.topic_name)
        except Exception as exe:
            raise ValueError(str(exe)) from exe
