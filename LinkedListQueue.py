from LinkedList import LinkedList


# TODO: coomplete the methods and put their time complexities in the comments
class LinkedListQueue:

    def __init__(self):
        # Create empty LinkedList to store queue items
        self.list = LinkedList()

    def enqueue(self, item):
        # Add item to back of queue (tail of list)
        self.list.append(item)

    def dequeue(self):
        # Remove and return item from front of queue (head of list)
        if self.is_empty():
            return None
        return self.list.delete_from_head()

    def peek(self):
        # Look at front item without removing it
        if self.is_empty():
            return None
        return self.list.head.data

    def is_empty(self):
        # Check if queue has any items
        return self.list.head is None

    def size(self):
        # Return number of items in queue
        count = 0
        current = self.list.head
        while current:
            count += 1
            current = current.next
        return count
