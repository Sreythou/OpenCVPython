import cv2 as cv
import numpy as np

img = cv.imread("../Resources/credit_card.jpg")
# print(img.shape)
imgResize = cv.resize(img,(600,600))

width, height = 350,300
pt1 = np.float32([[187,160],[509,361], [69,390],[394,600]]) # perspective of shape that we want to cut
pt2 = np.float32([[0,0], [width, 0], [0, height], [width, height]]) # New perspective
matrix = cv.getPerspectiveTransform(pt1,pt2)    # transform original wrap to the new size
imgOutput = cv.warpPerspective(imgResize, matrix, (width, height))

cv.imshow("Original", imgResize)
cv.imshow("Result", imgOutput)
cv.waitKey(0)