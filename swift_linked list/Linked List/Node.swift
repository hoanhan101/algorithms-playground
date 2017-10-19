//
//  Node.swift
//  Linked List
//
//  Created by Hoanh An on 10/10/17.
//  Copyright © 2017 Hoanh An. All rights reserved.
//

import Foundation

class Node<T: Equatable>: NSObject {
    var value: T
    var next: Node<T>?
    var prev: Node<T>?
    
    init(initialValue: T) {
        value = initialValue
    }
    
    override var description : String {
        return "\(value) \(next == nil ? "//" : "->" )"
    }
}
