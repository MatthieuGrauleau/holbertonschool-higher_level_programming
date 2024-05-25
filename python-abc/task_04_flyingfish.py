#!/usr/bin/env python3


class Fish:
    """This class represents a fish."""
    def swim(self):
        """This method makes the fish swim."""
        print("The fish is swimming")

    def habitat(self):
        """This method describes the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """This class represents a bird."""
    def fly(self):
        """This method makes the bird fly."""
        print("The bird is flying")

    def habitat(self):
        """This method describes the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """This class represents a flying fish."""
    def fly(self):
        """This method makes the flying fish soar."""
        print("The flying fish is soaring!")

    def swim(self):
        """This method makes the flying fish swim."""
        print("The flying fish is swimming!")

    def habitat(self):
        """This method describes the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
