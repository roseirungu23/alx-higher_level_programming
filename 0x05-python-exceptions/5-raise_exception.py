#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("This is a TypeError")
    except TypeError as error:
        print(f"Type error occurred: {error}")


raise_exception()
