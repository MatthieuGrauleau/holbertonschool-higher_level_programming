#!/usr/bin/python3
"""class Student that defines a student by"""


class Student:
    """
    Represents a student.

    Attributes:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student.
        """
        return self.__dict__
