import cv2 as cv

img = cv.imread("../Resources/pikachu.png")
cv.imshow("Pikachu Display Window", img)

cv.waitKey(2000)    # 2000 = 2seconds
