import cv2 as cv
import numpy as np

widthImg = 640
heightImg = 480
minArea = 500

cap = cv.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10, 150)

def preProcessing(img):
    imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv.Canny(imgBlur, 50, 50)
    # kernel = np.ones((5, 5))
    # imgDial = cv.dilate(imgCanny, kernel, iterations=2)
    # imgThres = cv.erode(imgDial, kernel, iterations=1)

    return imgCanny

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    _, contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > minArea:
            # cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)

            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv.drawContours(imgContour, biggest, -1, (255, 0, 0), 3)
    return biggest

def getWarp(img, biggest):

    pt1 = np.float32(biggest)
    pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv.getPerspectiveTransform(pt1, pt2)
    imgOutput = cv.warpPerspective(img, matrix, (widthImg, heightImg))

    return imgOutput

while True:
    success, img = cap.read()
    img = cv.resize(img, (widthImg, heightImg))
    imgContour = img.copy()

    imgThres = preProcessing(img)
    biggest = getContours(imgThres)

    imgWarp = getWarp(img, biggest)

    cv.imshow("Result", imgThres)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
