from LinkedList import LinkedList

# TODO: coomplete the methods and put their time complexities in the comments


class LinkedListStack:

    def __init__(self):
        # Create an empty LinkedList to store our stack items
        self.list = LinkedList()

    def push(self, item):
        # Add item to the "top" of stack (we'll use head of list as top)
        self.list.prepend(item)

    def pop(self):
        # Remove and return item from top of stack
        # Check if stack is empty first
        if self.is_empty():
            return None
        return self.list.delete_from_head()

    def peek(self):
        # Look at top item without removing it
        if self.is_empty():
            return None
        return self.list.head.data

    def is_empty(self):
        # Check if stack has any items
        return self.list.head is None

    def size(self):
        # Return number of items in stack
        count = 0
        current = self.list.head
        while current:
            count += 1
            current = current.next
        return count
