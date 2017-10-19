from node import *

class Stack(object):
    """
        Model Stack as a class.
    """
    def __init__(self, top=None):
        """
        Create an instance of Stack.
        :param top: The top node of stack.
        :return: Stack instance.
        """
        self.top = top

    def push(self, value):
        """
        Push a node on top of a stack.
        :param value: The value of a node to be pushed to a stack.
        :return: None.

        Complexity:
        - Time: O(1)
        - Space: O(1)
        """
        self.top = Node(value, self.top)

    def pop(self):
        """
        Remove the top node of a stack.
        :return: The value of that node

        Complexity:
        - Time: O(1)
        - Space: O(1)
        """
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Return the top value of a stack.
        :return: The top value of a stack.

        Complexity:
        - Time: O(1)
        - Space: O(1)
        """
        return self.top.value if self.top is not None else None

    def is_empty(self):
        """
        Check if the stack is empty.
        :return: True if it's empty, otherwise False

        Complexity:
        - Time: O(1)
        - Space: O(1)
        """
        return self.peek() is None