#!/usr/bin/env python3
"""Abstract Class"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """subclass named Dog"""
    def sound(self):
        return ("Bark")


class Cat(Animal):
    """subclass named Dog"""
    def sound(self):
        return ("Meow")
