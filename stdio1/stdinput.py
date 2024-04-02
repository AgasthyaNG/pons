import logging


def stand_io():
    value = []
    user_val = ""
    while True:
        user_val = str(input("Enter message: "))
        if user_val == "exit":
            break
        value.append(user_val)
    return value
