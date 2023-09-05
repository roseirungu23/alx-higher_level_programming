#!/usr/bin/python3
"""Defines a matrix division function."""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix containing integers or floats.
        div (int or float): The number to divide all matrix elements by.

    Returns:
        list of lists: A new matrix with elements divided by the number and rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats, if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to 0."""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
