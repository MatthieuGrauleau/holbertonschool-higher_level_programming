#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads and prints the contents of a file.
    Args:
    filename (str): The name of the file to be read.
    Returns:
    None"""
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
