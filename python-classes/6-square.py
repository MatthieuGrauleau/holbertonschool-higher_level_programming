#!/usr/bin/python3
"""Write an empty class """


class Square:
    """Define a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
             size (int): size of the square
             position (tuple): position of the square
         """
        self.size = size
        self.position = position

    @property
    def size(self):
        """current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """value is the lenght of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square.

        Args:
             value (tuple): the new position of the square

        Raises:
             TypeError: if position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the size of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]

        for i in range(self.__size):
            print("_" * self.__position[0] + "#" * self.__size)
