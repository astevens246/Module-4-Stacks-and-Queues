class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Implements a basic linked list"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete_from_head(self):
        # If list is empty, return None
        if self.head is None:
            return None

        # Save the data to return
        deleted_data = self.head.data

        # Move head to next node
        self.head = self.head.next

        # If list becomes empty, update tail too
        if self.head is None:
            self.tail = None

        # Return the deleted data
        return deleted_data

    def delete_from_tail(self):
        # If list is empty
        if self.head is None:
            return None

        # If only one node
        if self.head == self.tail:
            deleted_data = self.head.data
            self.head = None
            self.tail = None
            return deleted_data

        # Get to the node before tail
        current = self.head
        while current.next != self.tail:
            current = current.next

        # Save tail's data
        deleted_data = self.tail.data

        # Update tail
        self.tail = current
        current.next = None

        return deleted_data

    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
