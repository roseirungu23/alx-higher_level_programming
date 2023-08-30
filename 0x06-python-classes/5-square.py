#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square"""
    def __init__(self, size):
        """initialize a new square""
        Args:
        size(int): the size of the new square."""
        self.size = size

    @property
    def size(self):
        """Get the current size of the square.
        Return:
            int: the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the current area of the square"""
        return (self.__size * self.size)

    def my_print(self):
        """Print the square with '#' characters
        If size == 0, prints an empty line."""
        if size == 0:
            print()
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
