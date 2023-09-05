#!/usr/bin/python3
"""Define a function lazy_matrix_mul."""


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using Numpy

    Args:
        m_a(list of lists): the first matrix.
        m_b(list of lists): the second matrix.

    Raises:
        ValueError: if the matrices can't be multiplied."""

    return (np.matmul(m_a, m_b))
