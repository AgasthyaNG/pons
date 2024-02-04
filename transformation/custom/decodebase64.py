import base64
def decodebase64(msg) -> str:
    return(base64.b64decode(msg).decode("utf-8"))