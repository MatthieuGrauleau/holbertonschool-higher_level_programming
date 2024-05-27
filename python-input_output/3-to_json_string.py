#!/usr/bin/python3
""" function that returns the JSON
representation of an object (string):"""
import json


import json

def to_json_string(my_obj):
    """Convert a Python object to a JSON string representation.
    Args:my_obj: The Python object to be converted.
    Returns:A JSON string representation of the input object."""
    return json.dumps(my_obj)
