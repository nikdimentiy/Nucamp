class Stack:
    """
    A stack data structure.

    Attributes:
        size: The maximum size of the stack.
        stack: A list of items in the stack.

    Methods:
        push: Adds an item to the top of the stack.
        pop: Removes and returns the top item of the stack.
        peek: Returns the top item of the stack without removing it.
        is_empty: Returns True if the stack is empty, False otherwise.
        is_full: Returns True if the stack is full, False otherwise.
        clear: Removes all items from the stack.
    """

    def __init__(self, size):
        """
        Initialize the stack with a given size.

        Args:
            size: The maximum size of the stack.
        """
        self.size = size
        self.stack = []

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.stack)

    def __repr__(self):
        """Return a representation of the stack."""
        return str(self.stack)

    def __getitem__(self, key):
        """Return the item at the given index."""
        return self.stack[key]

    def __len__(self):
        """Return the length of the stack."""
        return len(self.stack)

    def __eq__(self, other):
        """Return True if the stack is equal to other, False otherwise."""
        return self.stack == other

    def __contains__(self, item):
        """Return True if item is in the stack, False otherwise."""
        return item in self.stack

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to add to the stack.

        Raises:
            IndexError: If the stack is full.
        """
        if len(self.stack) == self.size:
            raise IndexError("Stack is full")
        else:
            self.stack.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        else:
            return self.stack.pop()

    def peek(self):
        """
        Returns the top item of the stack without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        else:
            return self.stack[-1]

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return len(self.stack) == 0

    def is_full(self):
        """Returns True if the stack is full, False otherwise."""
        return len(self.stack) == self.size

    def clear(self):
        """Removes all items from the stack."""
        self.stack = []

