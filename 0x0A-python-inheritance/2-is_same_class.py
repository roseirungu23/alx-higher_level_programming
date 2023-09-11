#!/usr/bin/python3
"""
Defines function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly the same class and False otherwise"""
    return type(obj) is a_class
