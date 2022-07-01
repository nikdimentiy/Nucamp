class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self):
        value = str(self.value) + " "
        left = str(self.left or "")
        right = str(self.right or "")
        return value + left + right

    def insert(self, data):
        if self.data:
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
        else:
            self.data = data

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
