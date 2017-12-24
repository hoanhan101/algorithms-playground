//
//  PageCell.swift
//  FaceDetection
//
//  Created by Hoanh An on 8/21/17.
//  Based on LetsBuildThatApp's Face Detection
//  https://www.letsbuildthatapp.com/course_video?id=1572
//

import UIKit
import Vision

class PageCell: UICollectionViewCell {
    
    var imageName: String? {
        didSet {
            guard let imageName = imageName else { return }
            
            detectedFaces?.forEach { (v) in
                v.removeFromSuperview()
            }
            
            detectedFaces = nil
            
            imageView.image = UIImage(named: imageName)
        }
    }
    
    fileprivate let activityIndicatorView: UIActivityIndicatorView = {
        let aiv = UIActivityIndicatorView(activityIndicatorStyle: .whiteLarge)
        aiv.translatesAutoresizingMaskIntoConstraints = false
        return aiv
    }()
    
    let imageView: UIImageView = {
        let iv = UIImageView()
        iv.contentMode = .scaleAspectFit
        iv.translatesAutoresizingMaskIntoConstraints = false
        return iv
    }()
    
    var detectedFaces: [UIView]?
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        addSubview(imageView)
        imageView.leftAnchor.constraint(equalTo: leftAnchor).isActive = true
        imageView.topAnchor.constraint(equalTo: topAnchor).isActive = true
        imageView.rightAnchor.constraint(equalTo: rightAnchor).isActive = true
        imageView.bottomAnchor.constraint(equalTo: bottomAnchor).isActive = true
        
        addSubview(activityIndicatorView)
        activityIndicatorView.topAnchor.constraint(equalTo: topAnchor, constant: 50).isActive = true
        activityIndicatorView.centerXAnchor.constraint(equalTo: centerXAnchor).isActive = true
        
        addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(handleTap)))
    }
    
    @objc fileprivate func handleTap() {
        if detectedFaces?.count ?? 0 > 0 {
            detectedFaces?.forEach({$0.removeFromSuperview()})
            detectedFaces?.removeAll()
        } else {
            activityIndicatorView.startAnimating()
            detectFaces()
        }
    }
    
    private func detectFaces() {
        guard let image = imageView.image else { return }
        
        let imageScaledHeight = frame.size.width / image.size.width * image.size.height
        
        let request = VNDetectFaceRectanglesRequest { (req, err) in
            
            DispatchQueue.main.async {
                self.activityIndicatorView.stopAnimating()
            }
            
            self.detectedFaces = []
            req.results?.forEach({ (res) in
                
                guard let faceObservation = res as? VNFaceObservation else { return }
                DispatchQueue.main.async {
                    let rect = faceObservation.boundingBox
                    let transformFlip = CGAffineTransform.init(scaleX: 1, y: -1).translatedBy(x: 0, y: -imageScaledHeight - self.frame.height / 2 + imageScaledHeight / 2)
                    let transformScale = CGAffineTransform.identity.scaledBy(x: self.frame.width, y: imageScaledHeight)
                    let converted_rect = rect.applying(transformScale).applying(transformFlip)
                    
                    let redView = UIView()
                    redView.layer.borderColor = UIColor.red.cgColor
                    redView.layer.borderWidth = 2
                    redView.frame = converted_rect
                    self.addSubview(redView)
                    
                    redView.layer.transform = CATransform3DMakeScale(0, 0, 0)
                    
                    UIView.animate(withDuration: 0.5, delay: 0, usingSpringWithDamping: 0.5, initialSpringVelocity: 1, options: .curveEaseOut, animations: {
                        redView.layer.transform = CATransform3DMakeScale(1, 1, 1)
                    }, completion: nil)
                    
                    self.detectedFaces?.append(redView)
                }
            })
        }
        
        DispatchQueue.global(qos: .userInitiated).async {
            guard let cgImage = image.cgImage else { return }
            let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
            do {
                try requestHandler.perform([request])
            } catch let err {
                print("Failed to perform request", err)
            }
        }
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}
