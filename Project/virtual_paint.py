import cv2 as cv
import numpy as np

# Set up web cam
frameWidth = 640
frameHeight = 400
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Color from color picker
myColors = [[30, 107, 0, 19, 255, 255],      # Orange
            [133, 56, 0, 159, 156, 255],    # Purple
            [57, 76, 0, 100, 255, 255],
            [90, 48, 0, 118, 255, 255]]     # Green
myColorValues = [[51, 153, 255],
                  [255, 0, 255],
                  [0, 255, 0],
                 [255, 0, 0]]       # BGR
myPoints = [] #[x, y, colorID]

def findColor(img, myColors, myColorValues):
    count = 0
    newPoints = []
    imgHSV = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv.circle(imgResult, (x, y), 10, myColorValues[count], cv.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv.imshow(str(color[0]), mask)

    return newPoints

def getContours(img):
    # Contours: curve joining all the continuous points
    _, contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            # cv.drawContours(imgResult, cnt, -1, (255, 0, 0))
            arc = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * arc, True)
            x, y, w, h = cv.boundingRect(approx)    # bounding rectangle
    return x+w//2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for point in newPoints:
            myPoints.append(point)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv.imshow("Result", imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

