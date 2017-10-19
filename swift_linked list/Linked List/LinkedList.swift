//
//  LinkedList.swift
//  Linked List
//
//  Created by Hoanh An on 10/10/17.
//  Copyright © 2017 Hoanh An. All rights reserved.
//

import Foundation

class LinkedList<T: Equatable>: NSObject {
    var head: Node<T>?
    var tail: Node<T>?
    
    func insertAtHead(newNode: Node<T>) {
        if let headNode = head {
            newNode.next = headNode
            headNode.prev = newNode
        } else {
            tail = newNode
        }
        
        head = newNode
    }
    
    func insertAtTail(newNode: Node<T>) {
        if let tailNode = tail {
            tailNode.next = newNode
            newNode.prev = tailNode
        } else {
            head = newNode
        }
        
        tail = newNode
    }
    
    func insertAfter(_ node: Node<T>, newNode: Node<T>) {
        if node == tail {
            insertAtTail(newNode: newNode)
            return
        }
        
        let nextNode = node.next
        node.next = newNode
        newNode.prev = node
        newNode.next = nextNode
        nextNode?.prev = newNode
    }
    
    func removeHead() {
        head?.prev = nil
        head = head?.next
    }
    
    func removeTail() {
        tail = tail?.prev
        tail?.next = nil
    }
    
    func remove(node: Node<T>) {
        if node == head {
            removeHead()
            return
        }
        
        if node == tail {
            removeTail()
            return
        }
        
        let prevNode = node.prev
        let nextNode = node.next
        
        prevNode?.next = nextNode
        nextNode?.prev = prevNode
    }
    
    func at(index: Int) -> Node<T>? {
        var currentNode = head
        var counter = index
        while currentNode != nil {
            if counter == 0 {
                return currentNode
            }
            counter -= 1
            currentNode = currentNode!.next
        }
        return nil
    }
    
    var length: Int {
        var counter = 1
        if var currentNode = head {
            while case let nextNode? = currentNode.next {
                currentNode = nextNode
                counter += 1
            }
            return counter
        } else {
            return 0
        }
    }
    
    func removeAt(index: Int) {
        let currentNode = at(index: index)
        remove(node: currentNode!)
    }
    
    func append(list: LinkedList) {
        if list.length == 0 {
            print("You are appending an empty list")
            return
        }
        
        self.tail?.next = list.head
        list.head?.prev = self.tail
        
        self.tail = list.tail
    }
    
    func randomNode() -> Node<T>? {
        let randomNumber = Int(arc4random_uniform(UInt32(length)))
        let currentNumber = at(index: randomNumber)
        return currentNumber
    }
    
    func findFirst(key: T) -> Node<T>? {
        var counter = 1
        var currentNode = head
        while case let nextNode? = currentNode?.next {
            currentNode = nextNode
            if currentNode?.value == key {
                return currentNode
            }
            counter += 1
        }
        return nil
    }
    
    override var description : String
    {
        if head == nil
        {
            if tail != nil
            {
                return "There was a problem"
            }
            
            return "Empty list"
        }
        
        var tempNode = head
        var returnString = "Head: "
        while tempNode != nil
        {
            returnString += tempNode!.description + " "
            tempNode = tempNode!.next
        }
        returnString += "Tail: \(tail!)"
        return returnString
    }
    
}

