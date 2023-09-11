#!/usr/bin/python3
"""
Defines a class inherited_from
"""


def inherited_from(obj, a_class):
    """returns True if the object is an instance of a class that
    inherited from a_class, otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
