"""
    Is One Array a Rotation of Another? (Python)

    Write a function that returns True if one array is a rotation of another.
    Example: [1, 2, 3, 4, 5, 6, 7] is a rotation of [4, 5, 6, 7, 1, 2, 3].

    NOTE: There are no duplicates in each of these arrays.
    REMINDER: We're going to use lists instead of arrays in Python for simplicity.
"""

def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    temp_item = list1[0]
    temp_index = -1

    for index in range(len(list2)):
        if list2[index] == temp_item:
            temp_index = index
            break

    if temp_index == -1:
        return False

    for index in range(1, len(list1)):
        if temp_index == len(list2) - 1:
            temp_index = 0
        else:
            temp_index += 1

        if list1[index] != list2[temp_index]:
            return False

    return True

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2b = [4, 5, 6, 7, 1, 2, 3]
    print(is_rotation(list1, list2b)) # True

    list2c = [4, 5, 6, 9, 1, 2, 3]
    print(is_rotation(list1, list2c)) # False

    list2d = [4, 6, 5, 7, 1, 2, 3]
    print(is_rotation(list1, list2d)) # False

    list2e = [4, 5, 6, 7, 0, 2, 3]
    print(is_rotation(list1, list2e)) # False

    list2f = [1, 2, 3, 4, 5, 6, 7]
    print(is_rotation(list1, list2f)) # True

