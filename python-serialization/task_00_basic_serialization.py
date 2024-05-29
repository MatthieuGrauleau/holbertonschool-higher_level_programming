#!/usr/bin/python3
"""
Module for basic serialization and deserialization of Python dictionaries
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file.
        If the file already exists, it will be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        return json.load(file)
