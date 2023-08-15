#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_a) < 2:
        tuple_a = tuple_a + (0,)
    while len(tuple_b) < 2:
        tuple_b = tuple_b + (0,)
    a = tuple_a[:2]
    b = tuple_b[:2]
    result = (a[0] + b[0], a[1] + b[1])

    return result
