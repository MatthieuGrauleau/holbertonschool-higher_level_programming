#!/usr/bin/python3
class VerboseList(list):
    """
    A subclass of list that prints messages when modifying the list."""
    def append(self, item):
        """Appends an item to the list and prints a message.
        Args:item: The item to be appended to the list."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extends the list with the given items and prints a message.
        Args:items: An iterable of items to be added to the list."""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Removes the first occurrence of the
        item from the list and prints a message.
        Args:item: The item to be removed from the list."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        """Removes and returns the item at the
        specified index and prints a message.
        If no index is specified, the last item is removed and returned.
        Args: index: The index of the item to be
        removed. Default is -1 (last item).
        Returns:The removed item."""
        print("Popped [{}] from the list.".format(item))
        return item
