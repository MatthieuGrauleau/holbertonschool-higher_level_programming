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
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """current height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """value is the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
