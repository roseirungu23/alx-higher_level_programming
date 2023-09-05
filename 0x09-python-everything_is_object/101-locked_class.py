#!/usr/bin/python3
#101-locked_class.py

"""Defines a Locked Class."""


def LockedClass:
    """
    prevents the user from creating new instance attributes for 
    anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
