import cv2 as cv

img = cv.imread("../Resources/pikachu.png")
print(img.shape)    # (height, width) to get the size of the image

imgResize = cv.resize(img,(350,300))    # (width, height) to resize the image.
print(imgResize.shape)

imgCropped = img[50:250, 10:300]  # (height, width) to crop the image
print(imgCropped.shape)

cv.imshow("Original", img)
cv.imshow("Resize", imgResize)
cv.imshow("Cropped", imgCropped)
cv.waitKey(0)