# OpenCV has provide default Cascades
# Haarcascades contains trained classifiers for detecting objects of a particular type.
import cv2 as cv

face_cascade = cv.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")
img = cv.imread("../Resources/lisa.jpg")

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)

for(x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv.putText(img, "Face", (x, y - 5), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (250, 250, 50), 2)

cv.imshow("Image", img)
cv.waitKey(0)