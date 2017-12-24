//
//  ViewController.swift
//  FacebookLiveStreamAnimation
//
//  Created by Hoanh An on 8/20/17.
//  Based on LetsBuildThatApp's Facebook Live Stream Animation
//  https://www.letsbuildthatapp.com/course_video?id=1372
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(handleTap)))
        
    }
    
    func handleTap() {
        (0...10).forEach { (_) in
            generateAnimatedViews()
        }
    }
    
    fileprivate func generateAnimatedViews() {
        let imageSets = [#imageLiteral(resourceName: "thumbs_up"), #imageLiteral(resourceName: "heart"), #imageLiteral(resourceName: "angry"), #imageLiteral(resourceName: "haha"), #imageLiteral(resourceName: "sad")]
        let randomIndex = Int(arc4random_uniform(UInt32(imageSets.count)))
        let image = imageSets[randomIndex]
        
        let imageView = UIImageView(image: image)
        let dimension = 20 + drand48() * 10 //drand48 gives you a number between 0 to 1
        
        imageView.frame = CGRect(x: 0, y: 0, width: dimension, height: dimension)
        
        let animation = CAKeyframeAnimation(keyPath: "position")
        animation.path = customPath().cgPath
        animation.duration = 2 + drand48() * 3
        animation.fillMode = kCAFillModeForwards
        animation.isRemovedOnCompletion = false //remove when it's done animating
        animation.timingFunction = CAMediaTimingFunction(name: kCAMediaTimingFunctionEaseOut) //accelerate at the beginning, slow down at the end
        
        
        imageView.layer.add(animation, forKey: nil)
        view.addSubview(imageView)

    }

}

//create a custom curved path
func customPath() -> UIBezierPath {
    let path = UIBezierPath()
    
    path.move(to: CGPoint(x: 0, y: 200))
    
    let endPoint = CGPoint(x: 700, y: 200)
    
    
    //in order to generate the icon randomly, need to randomzie control point
    let randomYShift = 100 + drand48() * 300
    let cp1 = CGPoint(x: 200, y: 100 - randomYShift)
    let cp2 = CGPoint(x: 400, y: 300 + randomYShift)
    
    path.addCurve(to: endPoint, controlPoint1: cp1, controlPoint2: cp2)
    
    return path
}

class CurvedView: UIView {
    override func draw(_ rect: CGRect) {
        let path = customPath()
        path.lineWidth = 3
        path.stroke()
    }
}
