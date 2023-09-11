#!/usr/python3
"""
Defines class MyInt
"""


class MyInt(int):
    """rebels the operators"""
    def __eq__(self, other):
        """inverts == to !="""
        return int(self) != other

    def __ne__(self, other):
        """inverts != to =="""
        return int(self) == other
