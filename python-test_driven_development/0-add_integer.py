#!/usr/bin/python3
""" Function that add to integer"""
def add_integer(a, b=98):
    """ add two integer who firsted get casted into integer
        Args:
            a (int, float): first integer to be added
            b (int, float): second integer to be added
        Returns:
            int: the sum of a and b.
        Raises:
            TypeError: if a or b isn't an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
