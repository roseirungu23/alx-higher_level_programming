#!usr/bin/python3
"""Defines function say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    Prints a message with the given first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
