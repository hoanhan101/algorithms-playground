//
//  PageController.swift
//  FaceDetection
//
//  Created by Hoanh An on 8/21/17.
//  Based on LetsBuildThatApp's Face Detection
//  https://www.letsbuildthatapp.com/course_video?id=1572
//

import UIKit

class PageController: UICollectionViewController, UICollectionViewDelegateFlowLayout {
    
    let images = ["got", "bbt", "sv"]
    
    let cellId = "cellId"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        collectionView?.register(PageCell.self, forCellWithReuseIdentifier: cellId)
        
        collectionView?.isPagingEnabled = true
        if let layout = collectionViewLayout as? UICollectionViewFlowLayout {
            layout.scrollDirection = .horizontal
        }
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        return 0
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat {
        return 0
    }
    
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath) as! PageCell
        
        cell.imageName = images[indexPath.item]
        
        return cell
    }
    
    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return images.count
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: view.frame.width, height: view.frame.height)
    }
    
}
