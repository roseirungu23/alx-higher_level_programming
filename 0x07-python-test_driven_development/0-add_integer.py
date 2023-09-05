#!/usr/bin/python3
""" It is a "0-add_integer" module.
    The module has one function, add_integer(a, b)."""


def add_integer(a, b=98):
    """Return the addition of integers a and b.

    Float arguments are typecasted to integers before addition is performed.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
