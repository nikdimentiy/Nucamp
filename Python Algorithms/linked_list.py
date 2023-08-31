class Node:
    def __init__(self, data):
        """
        Initializes a new Node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None

    def __repr__(self):
        """
        Returns a string representation of the node's data.
        """
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        """
        Initializes a new LinkedList.

        Args:
            nodes: A list of data elements to initialize the linked list with.
        """
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        """
        Returns a string representation of the linked list.
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        Returns an iterator that traverses the linked list nodes.
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        """
        Adds a node to the beginning of the linked list.

        Args:
            node: The node to be added to the beginning.
        """
        node.next = self.head
        self.head = node

    def add_last(self, node):
        """
        Adds a node to the end of the linked list.

        Args:
            node: The node to be added to the end.
        """
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def remove_node(self, target_node_data):
        """
        Removes a node with the specified data from the linked list.

        Args:
            target_node_data: The data of the node to be removed.

        Raises:
            Exception: If the linked list is empty or the target node is not found.
        """
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")
