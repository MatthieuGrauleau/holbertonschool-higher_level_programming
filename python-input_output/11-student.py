#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attributes to include in the dictionary.
                          If None, all attributes are included.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        """
        Reloads the attributes of the Student instance from a JSON representation.

        Args:
            json (dict): A dictionary containing the attributes of the Student instance.

        Returns:
            None
        """
        for key in json:
            self.__dict__[key] = json[key]
