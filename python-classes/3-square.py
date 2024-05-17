#!/usr/bin/python3
"""Write an empty class """


class Square:
    """Define a square."""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
        size (int): size of a square
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the size of the square"""
        return (self.__size * self.__size)
