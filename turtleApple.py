import cv2 as cv
import numpy as np
import math
import turtle as tr
import time

tr.tracer(0,0)
tr.colormode(255)

def distance(cor1,cor2):
    return math.sqrt(abs(cor1[0]-cor2[0])**2+abs(cor1[1]-cor2[1])**2)

video_path = r'.\data\【東方】Bad Apple!! ＰＶ【影絵】.mp4'
cap = cv.VideoCapture(video_path)

sizeMultiplier = 6 # resolution (0 best)
turtleMultiplier = 4 #size of turtle output


avgFrameDelay = 0
avgDivisor = 1
frameTime = time.time()
while True:
    success, image = cap.read()
    if not success:
        break
    image = cv.resize(image,[int(image.shape[1]/sizeMultiplier),int(image.shape[0]/sizeMultiplier)])
    imageOutline = cv.Canny(image,10,100,1)
    outImg = np.zeros([image.shape[0],image.shape[1],3],np.uint8)
    points = []

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if imageOutline[y][x] == 255:
                points.append([x,y*-1])
    

    for i in range(len(points)):
        bestPoint = points[0]
        minDist = distance(bestPoint,tr.position())
        for point in points:
                if distance(point,tr.position()) <= minDist:
                    minDist = distance(point,tr.position())
                    bestPoint = point
                    tr.pendown()
        tr.goto(bestPoint[0]*turtleMultiplier,bestPoint[1]*turtleMultiplier)
        points.pop(points.index(bestPoint))
        #tr.setx(bestPoint[0]*3)
        #tr.sety(bestPoint[1]*-3)
    tr.pencolor((0,0,0))
    tr.update()
    
    avgFrameDelay += time.time()-frameTime
    avgDivisor += 1
    frameTime = time.time()

    tr.reset()
    tr.pensize(2)
    tr.setx(image.shape[1]*turtleMultiplier)
    tr.sety(image.shape[0]*turtleMultiplier*-1)
    tr.setx(0)
    tr.sety(0)
    tr.setx(image.shape[1]*turtleMultiplier)
    tr.sety(image.shape[0]*turtleMultiplier*-1)



    #cv.imshow('im',outImg)
    cv.imshow("orig",cv.resize(imageOutline,[int(image.shape[1]*sizeMultiplier),int(image.shape[0]*sizeMultiplier)]))
    cv.waitKey(1)

print(avgFrameDelay/avgDivisor)
#avgtime = 