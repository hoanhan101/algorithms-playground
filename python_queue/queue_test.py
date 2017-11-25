#!/usr/bin/env python3

"""
	queue_test.py - Queue UnitTest
	Author: Hoanh An (hoanhan@bennington.edu)
	Date: 10/18/2017
"""

from queue import *

import unittest

class TestQueue(unittest.TestCase):
    def test_dequeue_empty_queue(self):
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)

    def test_dequeue_one_element(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)

    def test_dequeue_more_than_one_element(self):
        queue = Queue()
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

def main():
    test_queue = TestQueue()
    test_queue.test_dequeue_empty_queue()
    test_queue.test_dequeue_one_element()
    test_queue.test_dequeue_more_than_one_element()

if __name__ == '__main__':
    main()