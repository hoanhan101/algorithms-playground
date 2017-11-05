"""
    Find the most frequently occurring item in an array.
    Example: The most frequently occurring item in [1, 3, 1, 3, 2, 1] is 1.

    If you're given an empty array, you should return null (in Java) or None (in Python).

    You can assume that there is always a single, unique value that appears most frequently unless the array is empty.
    For instance, you won't be given an array such as [1, 1, 2, 2].
    NOTE: We're going to use lists instead of arrays in Python for simplicity.
"""

def most_frequent(given_list):
    count_dict = {}
    max_count = 0
    max_item = None

    for item in given_list:
        if item not in count_dict:
            count_dict[item] = 1
        else:
            count_dict[item] += 1

        if count_dict[item] > max_count:
            max_count = count_dict[item]
            max_item = item
    return max_item

if __name__ == '__main__':
    list1 = [1, 3, 1, 3, 2, 1]
    print(most_frequent(list1)) # 1

    list2 = [3, 3, 1, 3, 2, 1]
    print(most_frequent(list2)) # 3

    list3 = []
    print(most_frequent(list3)) # None

    list4 = [0]
    print(most_frequent(list4)) # 0

    list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
    print(most_frequent(list5)) # -1