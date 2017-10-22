#!/usr/bin/env python3

"""
	linear_search.py - Linear Search Implementation
	Author: Hoanh An (hoanhan@bennington.edu)
	Date: 10/18/2017
"""

def linear_search(arr, x):
    for i in arr:
        if i == x:
            return True
    return False

if __name__ == '__main__':
    test_array = [1, 2, 3]

    if linear_search(test_array, 3):
        print("PASSED test_item_in_list")

    if linear_search(test_array, 5) == False:
        print("PASSED test_item_NOT_in_list")