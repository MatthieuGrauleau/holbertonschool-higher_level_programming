#!/usr/bin/python3
"""A class that wraps an iterator and keeps
track of the number of iterations"""


class CountedIterator:
    """A class that wraps an iterator and keeps
    track of the number of iterations"""
    def __init__(self, some_iterable):
        """Initialize the iterator and counter"""
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Return the current count"""
        return self.counter

    def __next__(self):
        """Override the next method to increment the counter"""
        try:
            i = next(self.iterator)
            self.counter += 1
            return i
        except StopIteration:
            raise StopIteration
