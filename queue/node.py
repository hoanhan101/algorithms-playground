class Node(object):
    """
        Model Node as a class.
    """
    def __init__(self, value, next=None):
        """
        Create an instance of Stack.
        :param value: The value of a node.
        :param next: The next node that it points to.
        :return: Node instance.
        """
        self.value = value
        self.next = next

