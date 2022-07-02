class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return self.items == other

    def __contains__(self, item):
        """Checks if an item is in the queue"""
        return item in self.items

    def is_empty(self):
        """Checks if a Queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Adds an element at the end of the Queue"""
        self.items.append(item)

    def dequeue(self):
        """Removes the element at the beginning of the queue"""
        self.items = self.items[1:]
        return self.items

    def peek(self):
        """Returns the element at the beginning of the queue"""
        return self.items[-1]

    def reverse(self):
        """Reverses the order of the elements in the queue"""
        self.items.reverse()
        return self.items
