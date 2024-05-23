#!/usr/bin/python3
""" class Square that inherits from Rectangle (9-rectangle.py):"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class square"""
    def __init__(self, size):
        """Instantiation with size"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of a square"""
        return (self.__size * self.__size)
