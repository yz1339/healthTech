# Music Cognition
For Lab2, we designed an active tack and a passive task to study if music have influence on cognition and sleep quality. 

## Active Task
There are two parts in the active task. The users will first listen to a randomly generated piece of music and then they can proceed to do a reaction time task. We built the first part upon extending ORKStep and we used ORKReactionTimeStep for our second part. To make sure the users listen to the music for at least 10 seconds, the "next" button (a button for them to go to the next step) will only show up 10 seconds after the music starting playing. 

## Passive Task
We applied AWARE framework to our passive task, which is to collect data regards sleep quality. 
For example, we collect screen usage data at the normal sleep time. Let's say if the screen is unlocked several time during the sleeping time, this person might not sleep well. 
And also we use AWARE to collect surrounding noises data as another criteria to decide if this person has a high sleeping quality or not. We set the silence threshold to 32 dB( decibels), which based on some research saying that if noises is higher than 32 dB, it might affect people's sleeping quality. 
Also we collect communication data, which is calls, texts, still in the normal sleeping time range, if they are making calls during that time, they might not have a high quality rest.
Based on these three main data, we can get a rough idea about a person's sleep quality data.

