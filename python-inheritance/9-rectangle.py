#!/usr/bin/python3
"""a class Reactangle that inherits from BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """are of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """ return, the following rectangle
        description: [Rectangle] <width>/<height>"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
