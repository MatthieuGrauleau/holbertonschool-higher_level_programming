#!/usr/bin/python3
"""Write an empty class """


class Square:
    """Define a square."""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
        size (int): size of a square
         """
        self.size = size

    @property
    def size(self):
        """current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """value is the lenght of the square"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        """Return the size of the square"""
        return (self.__size * self.__size)
