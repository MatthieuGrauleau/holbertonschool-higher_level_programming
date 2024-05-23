#!/usr/bin/env python3
"""Abstract Class"""


from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Class representing a shape."""
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    A class representing a circle.
    Attributes:
    radius (float): The radius of the circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        Returns:
        float: The area of the circle.
        """
        return (3.141592653589793 * self.radius**2)

    def perimeter(self):
        """
        Calculate the perimeter of the circle.
        Returns:
        float: The perimeter of the circle."""
        return (2 * 3.141592653589793 * self.radius)


class Rectangle(Shape):
    """
    Represents a rectangle shape.
    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
        int: The area of the rectangle.
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns:
        int: The perimeter of the rectangle."""
        return (2 * (self.width + self.height))


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.
    Args:
    shape: An object representing a shape.
    Returns:
    None"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
