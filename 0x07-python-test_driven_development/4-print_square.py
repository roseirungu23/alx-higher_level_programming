#!/usr/bin/python3
"""
Defines a function print_square."""

def print_square(size):
    """prints a square with the character # of the given size.
    
    Args:
    size (int): The size length of the square

    Raises:
    TypeError: If size is not an integer or if size is a float and less than 0.
    ValueError: If size is less than o."""
    if not isinstance (size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
