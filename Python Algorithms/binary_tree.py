class Node:
    """
    A class representing a node in a binary tree.

    Attributes:
    data (int): The data stored in the node.
    left (Node | None): The left child node or None if no left child.
    right (Node | None): The right child node or None if no right child.
    """

    def __init__(self, data):
        """
        Initialize a new Node with the given data.

        Args:
        data (int): The data to be stored in the node.
        """
        self.data = data
        self._left = None  # Initialize left child as None
        self._right = None  # Initialize right child as None

    def __str__(self):
        """
        Return a string representation of the node.

        Returns:
        str: A string in the format "data (left, right)".
        """
        left = str(self._left) if self._left else ""
        right = str(self._right) if self._right else ""
        return f"{self.data} ({left}, {right})"

    @property
    def left(self):
        """
        Get the left child node.

        Returns:
        Node | None: The left child node or None if no left child.
        """
        return self._left

    @left.setter
    def left(self, node):
        """
        Set the left child node.

        Args:
        node (Node | None): The left child node or None to remove the left child.

        Raises:
        ValueError: If node is not a Node instance or None.
        """
        if isinstance(node, Node) or node is None:
            self._left = node
        else:
            raise ValueError("Left child must be a Node instance or None")

    @property
    def right(self):
        """
        Get the right child node.

        Returns:
        Node | None: The right child node or None if no right child.
        """
        return self._right

    @right.setter
    def right(self, node):
        """
        Set the right child node.

        Args:
        node (Node | None): The right child node or None to remove the right child.

        Raises:
        ValueError: If node is not a Node instance or None.
        """
        if isinstance(node, Node) or node is None:
            self._right = node
        else:
            raise ValueError("Right child must be a Node instance or None")

    def insert(self, data):
        """
        Insert data into the binary tree rooted at this node.

        Args:
        data (int): The data to be inserted into the tree.
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary tree rooted at this node.

        Returns:
        list: A list of node data in ascending order.
        """
        res = []
        if self.left:
            res += self.left.inorder_traversal()
        res.append(self.data)
        if self.right:
            res += self.right.inorder_traversal()
        return res

# Example usage:
if __name__ == "__main__":
    root = Node(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)

    print("Inorder Traversal:")
    print(root.inorder_traversal())  # Output should be [3, 5, 7, 10, 15]
