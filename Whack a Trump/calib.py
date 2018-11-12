# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:58:33 2018

@author: Gilles Moenaert, Kobe Vandooren

"""

import numpy as np
import cv2
import glob
import os
path = "D:\Documents\AI project\Webcam foto's"
path2 = "D:\Documents\AI project\Gelukt"
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)


objpoints = [] 
imgpoints = []
 
images = glob.glob(os.path.join(path,'*.jpg'))
print(images)
i=1
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    
    ret, corners = cv2.findChessboardCorners(gray, (9,6),None)

    
    print(ret+i)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        
        img = cv2.drawChessboardCorners(img, (9,6), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)
        out = cv2.imwrite(os.path.join(path2,'ait'+str(i)+'.jpg'), img)
        i +=1
        
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
file = open("distortion.txt","w")
for l in dist:
    for c in l:
        file.write(str(c)+' ')
file.close
file = open("cameramatrix.txt", "w")
for l in mtx:
    for c in l:
        file.write(str(c)+' ')
    file.write('\n')
file.close()

print(dist)
print (mtx)


cv2.destroyAllWindows()