#!/usr/bin/env python3

"""
	priority_queue.py - Priority Queue Implementation
	Author: Hoanh An (hoanhan@bennington.edu)
	Date: 10/18/2017

	Based on Donne Martin's Priority Queue implementation at:
	http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/priority_queue/priority_queue_solution.ipynb
"""

import sys

class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        self.array.append(node)
        return self.array[-1]

    def extract_min(self):
        if not self.array:
            return None
        minimum = sys.maxsize
        for index, node in enumerate(self.array):
            if node.key < minimum:
                minimum = node.key
                minimum_index = index
        return self.array.pop(minimum_index)

    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj is obj:
                node.key = new_key
                return node
        return None