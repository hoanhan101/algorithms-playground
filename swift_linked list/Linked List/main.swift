//
//  main.swift
//  Linked List
//
//  Created by Hoanh An on 10/10/17.
//  Copyright © 2017 Hoanh An. All rights reserved.
//

import Foundation

var node1 = Node<Int>(initialValue: 1)
var node2 = Node<Int>(initialValue: 2)
var node3 = Node<Int>(initialValue: 3)
var node4 = Node<Int>(initialValue: 4)
var node5 = Node<Int>(initialValue: 5)
var node6 = Node<Int>(initialValue: 6)
var node7 = Node<Int>(initialValue: 7)
var node8 = Node<Int>(initialValue: 8)
var node9 = Node<Int>(initialValue: 9)
var node10 = Node<Int>(initialValue: 10)

var testList = LinkedList<Int>()
print(testList.description)

testList.insertAtHead(newNode: node1)
testList.insertAtTail(newNode: node3)
testList.insertAfter(node1, newNode: node2)
testList.insertAtTail(newNode: node4)
testList.insertAtTail(newNode: node5)
testList.insertAfter(node5, newNode: node6)

testList.removeHead()
testList.removeTail()
testList.remove(node: node3)


print(testList.length)

testList.removeAt(index: 0)

print(testList.description)

var testList2 = LinkedList<Int>()

testList.append(list: testList2)
testList2.insertAtTail(newNode: node7)
testList2.insertAtTail(newNode: node8)
testList2.insertAtTail(newNode: node9)
testList.append(list: testList2)
print(testList.description)

print(testList.randomNode())
print(testList.findFirst(key: 7))


