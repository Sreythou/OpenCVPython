import cv2 as cv
import numpy as np

img = np.zeros((500, 500,3),np.uint8)   # Create image with color black (0)
img[:] = 200,200,300    # Color the whole image, if we define number [:] we only set the color to that small part

cv.line(img,(100,20),(img.shape[1]-30, 200),(0,0,0),4)  # create line
cv.rectangle(img, (80,120),(250,200),(0,12,130),3)      # create rectangle
cv.circle(img, (400, 60),30,(100,0,20),2)               # create circle
cv.putText(img,"Khean Sreythou",(50,400), cv.FONT_HERSHEY_SIMPLEX,1.5,(250,250,50),3)

cv.imshow("Image", img)

cv.waitKey(0)