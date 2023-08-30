#!/usr/bin/python3
"""Define class square"""


class Square:
    """Represent the square"""
    def __init__(self, size=0, position(0, 0)):
        """initialize the new square
        Args:
        size(int): the size of the new square
        position(int, int): the position of the new square"""
        self.size = size
        self.position = position

        @property
        def size(self):
            """Get the current size of the square"""
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

        @property
        def position(self):
            """Set the position of the square"""
            return (self.__position)

        @position.setter
        def position(self, value):
            """Set the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If the value is not a tuple of two positive integers."""
            if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                    not all(num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 "
                                "positive integers")
        self.__position = value

        def area(self):
            """Calculate the area of the square"""
            return (self.__size * self.__size)

        def my_print(self):
            """Print the square with # characters"""
            if self.__size == 0:
                print()
                return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
