class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """Add a new node with the given value at the beginning of the linked list."""
        new_node = Node(value)

        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        # If the list is not empty, set the new node as the head and link it to the previous head
        new_node.next = self.head
        self.head = new_node
        print("Prepended new Head Node with value:", self.head.value)
        if self.head.next:
            print("Node following head is:", self.head.next.value)
        else:
            print("No node following head.")

    def append(self, value):
        """Add a new node with the given value at the end of the linked list."""
        new_node = Node(value)

        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        # Traverse the list to find the last node
        node = self.head
        while node.next is not None:
            node = node.next

        # Set the new node as the next node of the last node
        node.next = new_node
        print("Appended new Node with value:", node.next.value)


# Test the LinkedList class
llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")
