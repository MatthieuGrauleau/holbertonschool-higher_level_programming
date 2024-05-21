#!/usr/bin/python3
"""Prints a square with the character '#'.

    Args:
    size: The size length of the square, which must be an integer.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
