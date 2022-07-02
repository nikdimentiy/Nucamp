class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return str(self.stack)

    def __getitems__(self, key):
        return self.stack[key]

    def __len__(self):
        return len(self.stack)

    def __eq__(self, other):
        return self.stack == other

    def __contains__(self, item):
        return item in self.stack

    def push(self, item):
        """Adds an item to the top of the stack"""
        if len(self.stack) == self.size:
            raise IndexError("Stack is full")
        else:
            self.stack.append(item)

    def pop(self):
        """Removes and returns the top item of the stack"""
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        else:
            return self.stack.pop()

    def peek(self):
        """Returns the top item of the stack without removing it"""
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        else:
            return self.stack[-1]

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise"""
        return len(self.stack) == 0

    def is_full(self):
        """Returns True if the stack is full, False otherwise"""
        return len(self.stack) == self.size

    def clear(self):
        """Removes all items from the stack"""
        self.stack = []
