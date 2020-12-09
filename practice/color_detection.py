import cv2 as cv
import numpy as np

def empty(a):
    pass

path = "../Resources/orange.jpg"
img = cv.imread(path)
img = cv.resize(img, (300,300))
imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.namedWindow("TrackBars")             # Create a window with the name: TrackBars
cv.resizeWindow("TrackBars", 600, 250)   # Set the size of the window TrackBars

# Create Trackbar in TrackBars window
cv.createTrackbar("Hue Min", "TrackBars", 30, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 30, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 200, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 200, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 250, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 250, 255, empty)

# Cannot put in while loop, python will crash
# But if we don't put in while loop, the tracker bar seem useless
# while True:

h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
v_min = cv.getTrackbarPos("Val Min", "TrackBars")
v_max = cv.getTrackbarPos("Val Max", "TrackBars")
# print(h_min, h_max, s_min, s_max, v_min, v_max)

lower = np.array([h_min, s_min, v_min])
upper = np.array([h_max, s_max, v_max])
mask = cv.inRange(imgHSV, lower, upper)
imgResult = cv.bitwise_and(img, img, mask=mask)

# cv.imshow("Original", img)
# cv.imshow("HSV", imgHSV)
# cv.imshow("Mask", mask)
cv.imshow("Result", imgResult)

cv.waitKey(0)
