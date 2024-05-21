#!/usr/bin/python3
"""Write an empty class """


class Rectangle:
    """Define a Rectangle."""
    def __init__(self, width=0, height=0):
        """define a rectangle
        Args:
        width (int): width of the rectangle. Defaults to 0.
        height (int): height of the rectangle. Defaults to 0."""
        self.width = width
        self.height = height

        @property
        def width(self):
            """current width of the rectangle"""
            return (self.__width)

        @width.setter
        def width(self, value):
            """value is the lenght of the square"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """current height of the rectangle"""
            return (self.__height)

        @height.setter
        def height(self, value):
            """value is the lenght of the square"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
