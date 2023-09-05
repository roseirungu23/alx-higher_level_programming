#!/usr/bin/python3
"""Defines a function matrix_mul."""


def matrix_mul(m_a, m_b):
    """multiplies two matrices.

    Args:
    m_a(listof lists): the first matrix.
    m_b(list of lists): the second matrix.

    Raises:
        TypeError: if m_a or m_b is not a list of lists, empty,
                    or contains non-integer/float elements.
        ValueError: if m_a or m_b can't be multiplied."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise TypeError("m_b can't be empty")
    if not all((isinstance(element, int) or isinstance(element, float))
            for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should be contain only integers or floats")
    if not all((isinstance(element, int) or isnstance(element, float))
            for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    if notall(len(row) == len(m_a[o]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    inverted_b = []
    for i in range(len(m_b[0])):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][r])
        inverted_b.append(new.row)

        new_matrix = []
        for row in m_a:
            new_row = []
            for col in inverted_b:
                prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)
    return new_matrix
