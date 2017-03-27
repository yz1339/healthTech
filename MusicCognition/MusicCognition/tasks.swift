//
//  tasks.swift
//  MusicCognition
//
//  Created by Yating Zhan on 3/13/17.
//  Copyright © 2017 Yating Zhan. All rights reserved.
//

import UIKit
import ResearchKit

public var tasks: ORKOrderedTask{
    var steps = [ORKStep]()
    
    let instructionStep = ORKInstructionStep(identifier: "IntroStep")
    instructionStep.title = "The Music Recognition "
    instructionStep.text = "Please follow the steps to listen a piece of music first and conduct a reaction time game."
    steps += [instructionStep]
    
    let musicStep = MusicStep(identifier: "musicStep")
    musicStep.isOptional = true
    steps += [musicStep]
    
    
    
    let reactionStep = ORKReactionTimeStep(identifier: "reactionStep")
    reactionStep.minimumStimulusInterval = 0.2
    reactionStep.maximumStimulusInterval = 3.0
    reactionStep.numberOfAttempts = 10
    reactionStep.thresholdAcceleration = 1
    reactionStep.timeout = 3
    steps += [reactionStep]
    
    let summaryStep = ORKCompletionStep(identifier: "SummaryStep")
    summaryStep.title = "Thank you!"
    summaryStep.text = "Thank you for taking the steps!"
    steps += [summaryStep]
    
    
    return ORKOrderedTask(identifier: "SurveyTask", steps: steps)
    
}
