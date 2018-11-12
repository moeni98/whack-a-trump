# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:51:40 2018

@author: basti
"""

import cv2
import keyboard
import os
import time


path = "D:\Documents\AI project\Webcam foto's"
cap = cv2.VideoCapture(0)
i=1
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.waitKey(5)

    cv2.imshow('SnapshotTaker', rgb)
    if keyboard.is_pressed(' '):        
        out = cv2.imwrite(os.path.join(path, 'capture'+str(i)+'.jpg'), frame)        
        time.sleep(0.15)        
        print(i)
        i+=1
    if keyboard.is_pressed('q'):        
        break

cap.release()
cv2.destroyAllWindows()
