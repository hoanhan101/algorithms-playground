"""
Rotating a 2D Array by 90 Degrees (Python)

A 2-dimensional array is an array of arrays.

Implement a function that takes a square 2D array (# columns = # rows) and rotates it by 90 degrees.

Example:
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

->

[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]

When you are done, try implementing this function so that you can solve this problem in place. Solving it in place means that your function won't create a new array to solve this problem.  Instead, modify the content of the given array with O(1) extra space.

NOTE: For simplicity, we're going to represent a 2 dimensional array as a list of lists in Python.
"""

import copy


# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)
    # NOTE: To solve it in place, write this function so that you
    # won't have to create rotated.
    return rotated


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# rotate(a1, 3) should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
# rotate(a2, 4) should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]
