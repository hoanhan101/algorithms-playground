"""
    Common Elements in Two Sorted Arrays (Python)

    Write a function that returns the common elements (as an array) between two sorted arrays of integers (ascending order).
    Example: The common elements between [1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10] are [1, 4, 9].

    REMINDER: We're going to use lists instead of arrays in Python for simplicity.
"""


# Way 1: Use dict
def common_elements(list1, list2):
    result = []
    temp_dict = {}

    for item in list1:
        temp_dict[item] = 1

    for item in list2:
        if item in temp_dict:
            result.append(item)
    return result

# Way 2: Use pointers
# def common_elements(list1, list2):
#     p1 = 0
#     p2 = 0
#     result = []
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] == list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#             p2 += 1
#         elif list1[p1] > list2[p2]:
#             p2 += 1
#         else:
#             p1 += 1
#     return result


if __name__ == '__main__':
    list_a1 = [1, 3, 4, 6, 7, 9]
    list_a2 = [1, 2, 4, 5, 9, 10]
    print(common_elements(list_a1, list_a2)) # [1, 4, 9]

    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    print(common_elements(list_b1, list_b2)) # [1, 2, 9, 10, 12]

    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    print(common_elements(list_c1, list_c2)) # []