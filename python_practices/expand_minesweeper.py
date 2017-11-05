"""
Find Where to Expand in Minesweeper (Python)

Implement a function that turns revealed cells into -2 given a location the user wants to click.

For simplicity, only reveal cells that have 0 in them.  If the user clicks on any other type of cell (for example, -1 / bomb or 1, 2, or 3), just ignore the click and return the original field.  If a user clicks 0, reveal all other 0's that are connected to it.



Example 1:

Given field:
[[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 1, -1, 1, 0]]

Click location: (2, 2: row index = 2, column index = 2)

Resulting field:
[[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 1, -1, 1, 0]] (same as the given field)



Example 2:

Given field:
[[-1, 1, 0, 0],
[1, 1, 0, 0],
[0, 0, 1, 1],
[0, 0, 1, -1]]

Click location: (1, 3: row index = 1, column index = 3)

Resulting field:
[[-1, 1, -2, -2],
[1, 1, -2, -2],
[-2, -2, 1, 1],
[-2, -2, 1, -1]]



Your function should take:

field: The given field as a 2D array
num_rows / numRows: The number of rows in the given field
num_cols / numCols: The number of columns in the given field
given_i / givenI: The row index of the cell the user wants to click
given_j / givenJ: The column index of the cell the user wants to click


NOTE: For simplicity, arrays are represented as lists in Python
"""


# Implement your function below.
def click(field, num_rows, num_cols, given_i, given_j):
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 2, 2) should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 1, 4) should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# click(field2, 4, 4, 0, 1) should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

# click(field2, 4, 4, 1, 3) should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
