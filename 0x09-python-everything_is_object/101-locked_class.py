#!/usr/bin/python3
# 101-locked_class.py

"""Defines a locked class"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes, 
    except if the new instance attribute is called first_name.
    """
    __slots__ = ("first_name",)

    def __init__(self, first_name):
        self.first_name = first_name
