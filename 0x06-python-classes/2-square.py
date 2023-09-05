#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """initialize a new square

        Args:
        size(int): the size of the new square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size