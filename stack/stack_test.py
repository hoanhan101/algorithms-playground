#!/usr/bin/env python3

"""
	stack_test.py - Stack UnitTest
	Author: Hoanh An (hoanhan@bennington.edu)
	Date: 10/18/2017
"""

from stack import *

import unittest

class TestStack(unittest.TestCase):

    def test_empty_stack(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.pop(), None)

    def test_one_element(self):
        top = Node(5)
        stack = Stack(top)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.peek(), None)

    def test_more_than_one_element(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.is_empty(), True)


def main():
    test_stack = TestStack()
    test_stack.test_empty_stack()
    test_stack.test_one_element()
    test_stack.test_more_than_one_element()

if __name__ == '__main__':
    main()