# -*- coding: utf-8 -*-
"""
- We assumed that every one second has 30 frames
- So one minute has 60 seconds and 1800 frames
- You will go for all frames, but only choose the frames which its count in the series MOD with [1800, 1200, 600]
  , or any numbers you want
- That will choose a frame randomly every 20, 40, or 60 seconds 
"""


# Importing libraries
import cv2
import os
import numpy as np

#
'''
- The next two loops are used to go through any sub-directory in the given directory.

- As we directory has only Videos, we don't put IF Statement to check for videos _ You can add if You arn't sure.
'''
for dirname, _, filenames in os.walk('C:/Users/DELL/PycharmProjects/xcuteframes/videos'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
        #The img_counter is used to count the images taken from each videos
        img_counter = 1
        # The i is the frame counter
        i = 0
        cap = cv2.VideoCapture(os.path.join(dirname, filename))
        
        while (cap.isOpened()):
            ret, frame = cap.read()
            
            # Stop when finished or img_counter is 150
            if (ret == False) or img_counter ==200:
                break
            if i % np.random.choice([1800, 1200, 600]) == 0: #Randomly Every 20, 40, 60 sec
            
                cv2.imwrite(filename[:-4] + str(img_counter) + '.jpg', frame)
                img_counter += 1
             
            i += 1
        
        
        cap.release()
        cv2.destroyAllWindows()