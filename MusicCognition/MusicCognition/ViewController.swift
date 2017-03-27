//
//  ViewController.swift
//  MusicCognition
//
//  Created by Yating Zhan on 3/13/17.
//  Copyright © 2017 Yating Zhan. All rights reserved.
//

import UIKit
import ResearchKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    @IBAction func doTask(_ sender: Any) {
        let taskViewController = ORKTaskViewController(task: tasks
            , taskRun: nil)
        //taskViewController.delegate = self
        present(taskViewController, animated: true, completion: nil)
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

