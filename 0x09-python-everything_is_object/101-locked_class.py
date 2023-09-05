#!/usr/bin/python3
"""Defines class LockedClass."""


def LockedClass:
    """prevents the user from dynamically creating new instance attributes."""
    __slots__ = ("first_name",)
