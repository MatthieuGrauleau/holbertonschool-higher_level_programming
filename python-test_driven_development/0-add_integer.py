#!/usr/bin/python3
""" Function that add two integer
b is set by default to 98
we need to have an int or a float for a and b otherwise we raise an error
return the sum of a and b after casting them as an int
"""


def add_integer(a, b=98):
    """Args: a and b as an int or float
        Returns: sum of a and b as an integer
        Raises: TypeError: if a or b isn't an integer"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
