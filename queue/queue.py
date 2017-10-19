from node import *

class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = Node(value)
        # Empty list
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        # Empty list
        if self.head is None and self.tail is None:
            return None
        value = self.head.value
        # Remove only element from a one element list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return value
