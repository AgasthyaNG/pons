"""This program reads the msg.value sent up by the transformation function and decode it using base64 library
"""
import base64


def decodebase64(msg) -> str:
    """_summary_

    Args:
        msg (_type_): base 64 encoded string to be decoded

    Returns:
        str: decode data
    """
    return base64.b64decode(msg).decode("utf-8")
