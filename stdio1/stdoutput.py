"""Writes the messages to the command line
"""

import logging


def stdio(msg) -> None:
    """_summary_

    Args:
        msg (_type_): _description_

    Returns:
        _type_: _description_
    """
    if type(msg) != str:
        logging.info("Received message: %s", msg.decode("utf-8"))
    else:
        logging.info("Received message: %s", msg)
