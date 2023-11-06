import cv2 as cv
import numpy as np
import math
import turtle as tr

tr.tracer(0,0)


def distance(cor1,cor2):
    return math.sqrt(abs(cor1[0]-cor2[0])**2+abs(cor1[1]-cor2[1])**2)

video_path = r'.\data\【東方】Bad Apple!! ＰＶ【影絵】.mp4'
cap = cv.VideoCapture(video_path)

sizeMultiplier = 5

while True:
    success, image = cap.read()
    if not success:
        break
    image = cv.resize(image,[int(image.shape[0]/sizeMultiplier),int(image.shape[1]/sizeMultiplier)])
    imageOutline = cv.Canny(image,10,100,1)
    outImg = np.zeros([image.shape[0],image.shape[1],3],np.uint8)
    points = []
    usedPoints = []

    for y in range(len(imageOutline)):
        for x in range(len(imageOutline[y])):
            if imageOutline[y][x] > 0:
                points.append([x,y])
    
    
        
    #print(usedPoints)
    while len(points) != len(usedPoints):
        closest = []
        closestDist = -1
        for point in points:
            if point not in usedPoints:
                if distance(point,tr.position()) < closestDist or closestDist == -1:
                    usedPoints.append(point)
                    closest = point
                    closestDist = distance(point,tr.position())
        #print(closest)
        tr.goto(closest[0]*-1,closest[1]*-1)
            
    tr.update()
    tr.reset()

    #cv.imshow('im',outImg)
    cv.imshow("orig",imageOutline)
    cv.waitKey(1)