import cv2 as cv
import numpy as np

img = cv.imread("../Resources/pikachu.png")

# Both of the images need to have the same matric
imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv.imshow("Horizontal", imgHor)
cv.imshow("Vertical", imgVer)

cv.waitKey(0)