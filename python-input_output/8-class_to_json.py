#!/usr/bin/python3


def class_to_json(obj):
    """Converts a Python object to a dictionary representation.
    Args:obj: The object to be converted.
    Returns:A dictionary representation of the object."""
    return obj.__dict__
