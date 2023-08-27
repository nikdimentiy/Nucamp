"""
A queue is a data structure that follows the FIFO (first-in, first-out) principle.

This class implements a queue using a list.
"""


class Queue:
    """
    Initialize a new queue.
    """

    def __init__(self):
        self.items = []

    """
    Get a string representation of the queue.
    """

    def __repr__(self):
        return str(self.items)

    """
    Get the item at the specified index.
    """

    def __getitem__(self, key):
        return self.items[key]

    """
    Get the length of the queue.
    """

    def __len__(self):
        return len(self.items)

    """
    Compare two queues.
    """

    def __eq__(self, other):
        return self.items == other

    """
    Check if an item is in the queue.
    """

    def __contains__(self, item):
        """Checks if an item is in the queue"""
        return item in self.items

    """
    Check if a Queue is empty.
    """

    def is_empty(self):
        """Checks if a Queue is empty"""
        return self.items == []

    """
    Add an element at the end of the queue.
    """

    def enqueue(self, item):
        """Adds an element at the end of the Queue"""
        self.items.append(item)

    """
    Removes the element at the beginning of the queue.
    """

    def dequeue(self):
        """Removes the element at the beginning of the queue"""
        self.items = self.items[1:]
        return self.items

    """
    Returns the element at the beginning of the queue.
    """

    def peek(self):
        """Returns the element at the beginning of the queue"""
        return self.items[-1]

    """
    Reverses the order of the elements in the queue.
    """

    def reverse(self):
        """Reverses the order of the elements in the queue"""
        self.items.reverse()
        return self.items


# Driver code

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("The queue is:", queue)

print("The first item in the queue is:", queue.peek())

print("Dequeueing an item from the queue:", queue.dequeue())

print("The queue is now:", queue)

print("The queue is empty:", queue.is_empty())
