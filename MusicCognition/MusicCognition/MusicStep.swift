//
//  MusicStep.swift
//  MusicCognition
//
//  Created by Yating Zhan on 3/13/17.
//  Copyright © 2017 Yating Zhan. All rights reserved.
//

import UIKit
import ResearchKit

class MusicStep: ORKStep {

//    var difficulty: Int = 1
//    var maxResponseTime: TimeInterval = 5.0

    static func stepViewControllerClass() -> AnyClass {
        return RSMusicGameStepViewController.self
    }
}

