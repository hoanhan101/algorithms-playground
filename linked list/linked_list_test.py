from linked_list import *

import unittest

class TestLinkedList(unittest.TestCase):
    def test_insert_to_front_empty_list(self):
        linked_list = LinkedList(None)
        linked_list.insert_to_front(10)
        self.assertEqual(linked_list.get_all_data(), [10])

    def test_insert_to_front_none(self):
        linked_list = LinkedList(None)
        linked_list.insert_to_front(None)
        self.assertEqual(linked_list.get_all_data(), [])

    def test_insert_to_front_mutiple_elements(self):
        linked_list = LinkedList(None)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(linked_list.get_all_data(), ['bc', 'a'])

    def test_append_empty_list(self):
        linked_list = LinkedList(None)
        linked_list.append(10)
        self.assertEqual(linked_list.get_all_data(), [10])

    def test_append_none(self):
        linked_list = LinkedList(None)
        linked_list.append(None)
        self.assertEqual(linked_list.get_all_data(), [])

    def test_append_multiple_elements(self):
        linked_list = LinkedList(None)
        linked_list.append('a')
        linked_list.append('bc')
        self.assertEqual(linked_list.get_all_data(), ['a', 'bc'])

    def test_find_empty_list(self):
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        self.assertEqual(node, None)

    def test_find_none(self):
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        self.assertEqual(node, None)

    def test_find_match(self):
        linked_list = LinkedList(None)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        self.assertEqual(str(node), 'a')

    def test_find_no_match(self):
        linked_list = LinkedList(None)
        node = linked_list.find('aaa')
        self.assertEqual(node, None)

    def test_delete_empty_list(self):
        linked_list = LinkedList(None)
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), [])

    def test_delete_none(self):
        linked_list = LinkedList(None)
        linked_list.delete(None)
        self.assertEqual(linked_list.get_all_data(), [])

    def test_delete_match(self):
        linked_list = LinkedList(None)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), ['bc'])

    def test_delete_no_match(self):
        linked_list = LinkedList(None)
        linked_list.delete('aa')
        self.assertEqual(linked_list.get_all_data(), [])

    def test_len_empty_list(self):
        linked_list = LinkedList(None)
        self.assertEqual(len(linked_list), 0)

    def test_len_multiple_elements(self):
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(len(linked_list), 3)

def main():
    test_linked_list = TestLinkedList()
    test_linked_list.test_insert_to_front_empty_list()
    test_linked_list.test_insert_to_front_none()
    test_linked_list.test_insert_to_front_mutiple_elements()
    test_linked_list.test_append_empty_list()
    test_linked_list.test_append_none()
    test_linked_list.test_append_multiple_elements()
    test_linked_list.test_find_empty_list()
    test_linked_list.test_find_none()
    test_linked_list.test_find_match()
    test_linked_list.test_find_no_match()
    test_linked_list.test_delete_empty_list()
    test_linked_list.test_delete_none()
    test_linked_list.test_delete_match()
    test_linked_list.test_delete_no_match()
    test_linked_list.test_len_empty_list()
    test_linked_list.test_len_multiple_elements()

if __name__ == '__main__':
    main()