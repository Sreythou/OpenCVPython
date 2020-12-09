import cv2 as cv
import numpy as np

img = cv.imread("../Resources/pikachu.png")
kernel = np.ones((5,5), np.uint8)

# Convert color of image to different color base on color base that define
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Convert to blur image
imgBlur = cv.GaussianBlur(imgGray, (7,7),0)

# Convert to canny edge image
imgCanny = cv.Canny(img, 150, 200)

# Convert to dilation image, more iterations more edge
imgDilation = cv.dilate(imgCanny, kernel, iterations=1)

# Convert to erode image (binary image), opposite from dilation image
imgErode = cv.erode(imgDilation, kernel, iterations=1)

cv.imshow("Gray Image", imgGray)
cv.imshow("Blur Image", imgBlur)
cv.imshow("Canny Image", imgCanny)
cv.imshow("Dilation Image", imgDilation)
cv.imshow("Erode Image", imgErode)

cv.waitKey(0)