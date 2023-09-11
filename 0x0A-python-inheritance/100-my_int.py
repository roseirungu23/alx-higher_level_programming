#!/usr/bin/python3
"""
Defines a class MyInt
"""


class MyInt(int):
    """
    MyInt class that inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverted equality operator.

        Args:
            other: The value to compare with.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality operator.

        Args:
            other: The value to compare with.
        """
        return super().__eq__(other)
