import base64


def tobytes(msg) -> str:
    """_summary_

    Args:
        msg (_type_): base 64 encoded string to be decoded

    Returns:
        str: decode data
    """
    return bytes(msg, "utf-8")
