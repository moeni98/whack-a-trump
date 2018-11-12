# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:56:24 2018

@author: basti
"""

import numpy as np
import time
import pygame
import random
import cv2
import cv2.aruco as aruco


whack = cv2.imread("Whack.png",cv2.IMREAD_UNCHANGED)
created = cv2.imread("created.png",cv2.IMREAD_UNCHANGED)
health = cv2.imread("heart.png",cv2.IMREAD_UNCHANGED)
Kobe = cv2.imread("Kobe.png",cv2.IMREAD_UNCHANGED)
Bastien = cv2.imread("Bastien.png",cv2.IMREAD_UNCHANGED)
Gilles = cv2.imread("Gilles.png",cv2.IMREAD_UNCHANGED)

file = open("distortion.txt", "r")
dist=np.zeros([5], float)
line=file.readline()
i =0
for l in line.split():
        dist[i] = float(l)
        i+=1          
        
file = open("cameramatrix.txt", "r")
mtx=np.zeros([3,3], float)
for l in range(0,3):
    line=file.readline()
    i=0
    for r in line.split():
        mtx[l,i]=r
        i+=1
        
# function to overlay a transparent image on backround.
def transparentOverlay(src , overlay , pos=(0,0),scale = 1):
    """
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image to be blit.
    :param scale : scale factor of transparent image.
    :return: Resultant Image
    """
    overlay = cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    h,w,_ = overlay.shape  # Size of pngImg
    rows,cols,_ = src.shape  # Size of background Image
    y,x = pos[0],pos[1]    # Position of PngImage
    
    #loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x+i >= rows or y+j >= cols:
                continue
            alpha = float(overlay[i][j][3]/255.0) # read the alpha channel 
            src[x+i][y+j] = alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]
    return src


def trumpid(corners,markerid,ids):
    for i in range(0,len(ids),1):      #convert markerid naar index
            if ids[i][0] == markerid:
                markerid = i
                break
     
    while True:
        try:
            corners = list(corners[markerid].ravel())
            corner = corners[:2]            
            x = corner[0]
            y = corner[1]
            return int(x),int(y)
        except:
            return False,False         

def trumpface():
    rand = random.randint(1, 8)
    if rand == 1:
        trump = cv2.imread("trump1.png",cv2.IMREAD_UNCHANGED)
    if rand == 2:
        trump = cv2.imread("trump2.png",cv2.IMREAD_UNCHANGED)
    if rand == 3:
        trump = cv2.imread("trump3.png",cv2.IMREAD_UNCHANGED)
    if rand == 4:
        trump = cv2.imread("trump4.png",cv2.IMREAD_UNCHANGED)
    if rand == 5:
        trump = cv2.imread("trump5.png",cv2.IMREAD_UNCHANGED)
    if rand == 6:
        trump = cv2.imread("trump6.png",cv2.IMREAD_UNCHANGED)
    if rand == 7:
        trump = cv2.imread("trump7.png",cv2.IMREAD_UNCHANGED)
    if rand == 8:
        trump = cv2.imread("trump8.png",cv2.IMREAD_UNCHANGED)
    return trump

def quote():
    rand = random.randint(1, 4)
    if rand == 1:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('quote1.ogg')
        sound.play()
    if rand == 2:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('quote2.ogg')
        sound.play()    
    if rand == 3:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('quote3.ogg')
        sound.play()  
    if rand == 4:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('quote4.ogg')
        sound.play()
    if rand == 5:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('quote5.ogg')
        sound.play() 
    if rand == 6:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('quote6.ogg')
        sound.play()  
    if rand == 7:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('quote7.ogg')
        sound.play()  
    if rand == 8:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('quote8.ogg')
        sound.play()  
    return quote

def highscore(score):
    naam = raw_input('Name:')
    file= open('highscores', 'r+')
    file.write(naam + ',' + str(score) +'/n')
    score0 = 0
    while(True):
        line = file.readline()
        naam, score = line.split(',')
        score = int()
        score0 = score
        if score > score0:
            hs = score
            nm = naam 
        check = file.readline()
        if check == '':
            file.close()
            break
    return hs, nm
            
    

cap = cv2.VideoCapture(0)
  
timer =  20
score = 0
lenids=[0]
ids0 = [0]
x = False
y = False
markerid = False
ret, frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_50)
parameters = aruco.DetectorParameters_create()
 #lists of ids and the corners beloning to each id
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
ids0 = np.copy(ids)

b = -130
c=0.1
i = 0
while(True):
    ret, frame = cap.read()
    if b > -400:
        frame = cv2.flip(frame,1)
        frame = transparentOverlay(frame,whack ,(28, b),0.4)
        b -= 20
    else:
        frame = cv2.flip(frame,1)
        frame = transparentOverlay(frame,whack ,(28, b),0.4)
        frame = transparentOverlay(frame,created ,(40, 150),c)
        frame = transparentOverlay(frame,Kobe ,(180, 150),c)
        frame = transparentOverlay(frame,Bastien ,(370, 150),c)
        frame = transparentOverlay(frame,Gilles ,(180, 180),c)
        if c < 0.3:
            c+=0.1
            
    if i > 18 and i % 2 == 0:       
        cv2.putText(frame, "Press S to play", (180, 380), cv2.FONT_HERSHEY_SIMPLEX,  0.8, (0, 255, 0), 2, cv2.LINE_AA)
    
    if i == 0:
        pygame.init()
        pygame.mixer.music.load('Loading.ogg')  
        pygame.mixer.music.play(-1)
    cv2.imshow('Whack a Trump',frame)
    i += 1
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

pygame.mixer.music.stop()
time.sleep(0.05)
pygame.init()
pygame.mixer.music.load('Trumpsong.ogg')  
pygame.mixer.music.play(-1)

Timer = 20
t=1
flipped = 0
lives = 3
l = 0
while (True):
    juistearucoweg = ''
    score1 = score
    ret, frame = cap.read()
    # operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_50)
    parameters = aruco.DetectorParameters_create()

    #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)    

    try:
        if np.all(ids != None) and lives >= 1:
               
            rvec, tvec,_ = aruco.estimatePoseSingleMarkers(corners[0], 0.05, mtx, dist) #Estimate pose of each marker and return the values rvet and tvec---different from camera coefficients
            #(rvec-tvec).any() # get rid of that nasty numpy value array error
            #aruco.drawAxis(frame, mtx, dist, rvec[0], tvec[0], 0.1) #Draw Axis
            aruco.drawDetectedMarkers(frame, corners) #Draw A square around the markers
            
            if len(ids)<len(ids0):
                juistearucoweg = True
                for i in range(0,len(ids)):
                    if ids[i]==markerid:
                        juistearucoweg = False
    
                        
            if juistearucoweg == True:
                i = markerid            
                try :
                    while i == markerid:
                       markerid = random.choice(ids.ravel())
                       
                except:                
                    markerid = ids.ravel()[0]                
                x , y = trumpid(corners,markerid,ids)
                trump = trumpface()
                score +=1
                timer = Timer*t           
                    
            timer-=1         
            if timer <= 0:
                i = markerid
                try :                
                    while i == markerid:
                        markerid = random.choice(ids.ravel())
                except:                
                    markerid = ids.ravel()[0]                                           
                x , y = trumpid(corners,markerid,ids)
                trump = trumpface()
                if score > 0:  
                    score -= 1
                    flipped -=1
                if l != 0:
                    lives -= 1
                l = 1
                    
                
                timer += Timer*t
            
            if x != False and y != False :
                    frame = transparentOverlay(frame,trump,(x-15,y-30),0.4)
                
            ids0 = np.copy(ids)
    except:
        pass
    if 10 <= flipped <=20 and lives != 0:
        cv2.putText(frame, "FLIPPED", (200, 125), cv2.FONT_HERSHEY_SIMPLEX,  2, (0, 800, 60), 2, cv2.LINE_AA)
        frame = cv2.flip(frame,1)
        if flipped == 20:
            t -= 0.1
            quote()
            flipped = 0
    
    frame = cv2.flip(frame,1)
    if score > score1:
        flipped += 1
        
    lx = 0
    for i in range(0, lives, 1):
        frame = transparentOverlay(frame,health ,(50 + lx, 100),0.2)
        lx += 35
    if lives >= 1:
        cv2.putText(frame, "Timer:{}".format(timer), (500, 75), cv2.FONT_HERSHEY_SIMPLEX,  0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "Score:{}".format(score), (45, 75), cv2.FONT_HERSHEY_SIMPLEX,  0.8, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        hs, nm = highscore(score)
        cv2.putText(frame, "GAME OVER !", (250, 125), cv2.FONT_HERSHEY_SIMPLEX,  0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "Highscore: "+ nm + ' '+ hs, (100, 100), cv2.FONT_HERSHEY_SIMPLEX,  0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "Score:{}".format(score+1), (260, 155), cv2.FONT_HERSHEY_SIMPLEX,  0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "Press Q to quit", (45, 400), cv2.FONT_HERSHEY_SIMPLEX,  0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "Hold S to Replay", (390, 400), cv2.FONT_HERSHEY_SIMPLEX,  0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Whack a Trump',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        lives = 3
        flipped = 0
        score = 0
        t = 1
    
pygame.mixer.music.stop()  
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


