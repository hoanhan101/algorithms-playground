"""
Is This a Binary Search Tree? (Python)

Write a function that takes a binary tree and returns true if it is a binary search tree, and false if not.

In our test code, we're going to use the following examples:

head1 = 0
       / \
      1   2
     /\   /\
    3  4 5  6
head1 is NOT a binary search tree.

head2 = 3
      /   \
     1     4
    /\    / \
   0  2  5   6
head2 is NOT a binary search tree.

head3 = 3
      /   \
     1     5
    /\    / \
   0  2  4   6
head3 is a binary search tree.

head4 = 3
      /   \
     1     5
    /\
   0  4
head4 is NOT a binary search tree.
"""

# Use this class to create binary trees.
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


# Implement your function below.
def is_bst(node, lower_lim=None, upper_lim=None):
    return False


# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


# NOTE: The following values will be used for testing your solution.

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
mapping4 = {3: [1, 5], 1: [0, 4]}
head1 = create_tree(mapping1, 0)
# This tree is:
#  head1 = 0
#        /   \
#       1     2
#      /\    / \
#     3  4  5   6
head2 = create_tree(mapping2, 3)
# This tree is:
#  head2 = 3
#        /   \
#       1     4
#      /\    / \
#     0  2  5   6
head3 = create_tree(mapping3, 3)
# This tree is:
#  head3 = 3
#        /   \
#       1     5
#      /\    / \
#     0  2  4   6
head4 = create_tree(mapping4, 3)
# This tree is:
#  head4 = 3
#        /   \
#       1     5
#      /\
#     0  4

# is_bst(head1) should return False
# is_bst(head2) should return False
# is_bst(head3) should return True
# is_bst(head4) should return False