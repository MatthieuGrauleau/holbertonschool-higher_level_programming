#!/usr/bin/python3
"""A class representing a custom object."""
import pickle


class CustomObject:
    """
    A class representing a custom object.

    Attributes:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Indicates whether the
            object is a student or not.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the details of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
                filename (str): The name of the file
                to save the serialized object to.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
                filename (str): The name of the file
                to deserialize the object from.

        Returns:
                CustomObject: The deserialized object,
                or None if deserialization fails.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
