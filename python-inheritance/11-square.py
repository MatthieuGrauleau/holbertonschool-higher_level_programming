#!/usr/bin/python3
""" class Square that inherits from Rectangle (9-rectangle.py):"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class square"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """are of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """ return, the following Square
        description: [Square] <size>/<size>"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
