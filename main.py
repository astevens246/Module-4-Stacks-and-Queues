from LinkedList import LinkedList
from LinkedListStack import LinkedListStack
from LinkedListQueue import LinkedListQueue

"""ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.prepend("X")
ll.prepend("Z")

ll.delete_from_head()
ll.delete_from_head()

ll.delete_from_tail()

ll.print_list()"""

# TODO: test out stack

# TODO: test out queue

# Test LinkedListStack
print("Testing Stack:")
stack = LinkedListStack()

# Push some items
stack.push("A")
stack.push("B")
stack.push("C")

print("Stack size:", stack.size())  # Should print 3
print("Top item:", stack.peek())  # Should print "C"

# Pop items
print("Popped:", stack.pop())  # Should print "C"
print("Popped:", stack.pop())  # Should print "B"
print("Stack size:", stack.size())  # Should print 1

# Test LinkedListQueue
print("\nTesting Queue:")
queue = LinkedListQueue()

# Enqueue some items
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Should print 3
print("Front item:", queue.peek())  # Should print 1

# Dequeue items
print("Dequeued:", queue.dequeue())  # Should print 1
print("Dequeued:", queue.dequeue())  # Should print 2
print("Queue size:", queue.size())  # Should print 1
