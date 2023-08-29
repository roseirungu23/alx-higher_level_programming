#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as error:
        print(f"NameError: {error}")

try:
    raise_exception_msg("Python is awesome.")
except NameError as ne:
    print(ne)
