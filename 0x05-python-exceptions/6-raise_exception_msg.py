#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as error:
        print(f"NameError: {error}")


raise_exception_msg("Python is awesome.")
