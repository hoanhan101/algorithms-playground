//
//  ViewController.swift
//  MagicalGrid
//
//  Created by Hoanh An on 8/21/17.
//  Copyright © 2017 Hoanh An. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    let numViewPerRow = 15

    var cells = [String: UIView]()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        let width = view.frame.width / CGFloat(numViewPerRow)

        
        for j in 0...30 {
            for i in 0...numViewPerRow {
                let cellView = UIView()
                cellView.backgroundColor = randomColor()
                cellView.frame = CGRect(x: CGFloat(i) * width, y: CGFloat(j) * width, width: width, height: width)
                cellView.layer.borderWidth = 0.5
                cellView.layer.borderColor = UIColor.black.cgColor
                view.addSubview(cellView)
                
                // Store location of each cellView to a dictionary
                let key = "\(i)|\(j)"
                cells[key] = cellView
            }
        }
        
        view.addGestureRecognizer(UIPanGestureRecognizer(target: self, action: #selector(handlePan)))
        
    }
    
    var selectedCell: UIView?
    
    func handlePan(gesture: UIPanGestureRecognizer) {
        let location = gesture.location(in: view)
        
        let width = view.frame.width / CGFloat(numViewPerRow)
        
        // Caculate location of a cellView base on pan gesture
        let i = Int(location.x / width)
        let j = Int(location.y / width)
        print(i, j)
        
        let key = "\(i)|\(j)"
        guard let cellView = cells[key] else { return }

        if selectedCell != cellView {
            UIView.animate(withDuration: 0.5, delay: 0, usingSpringWithDamping: 1, initialSpringVelocity: 1, options: .curveEaseOut, animations: { 
                self.selectedCell?.layer.transform = CATransform3DIdentity
            }, completion: nil)
        }
        
        selectedCell = cellView
        
        view.bringSubview(toFront: cellView)
        
        UIView.animate(withDuration: 0.5, delay: 0, usingSpringWithDamping: 1, initialSpringVelocity: 1, options: .curveEaseOut, animations: {
            cellView.layer.transform = CATransform3DMakeScale(3, 3, 3)
        }, completion: nil)
        
        
        // Add Bounce Effect
        if gesture.state == .ended {
            UIView.animate(withDuration: 0.5, delay: 0.25, usingSpringWithDamping: 0.5, initialSpringVelocity: 0.5, options: .curveEaseOut, animations: { 
                cellView.layer.transform = CATransform3DIdentity
            }, completion: nil)
        }
        
        

        // This is bad implementation since it need to loop a lot of time.
        // Above is the optimization using hash map dictionary
        // ----------------------------------------------------------------
        // var loopCount = 0
        // for subView in view.subviews {
        //     if subView.frame.contains(location) {
        //        subView.backgroundColor = .black
        //     }
        //     loopCount += 1
        // }
    }
    
    fileprivate func randomColor() -> UIColor {
        let red = CGFloat(drand48())
        let green = CGFloat(drand48())
        let blue = CGFloat(drand48())

        
        return UIColor(red: red, green: green, blue: blue, alpha: 1)
    }
    

}

