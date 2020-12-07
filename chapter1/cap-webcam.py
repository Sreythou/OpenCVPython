import cv2 as cv

cap = cv.VideoCapture(0)  # 0 is an id of webcam. If more than 1, we can define other number.

# Setting web cam parameters
cap.set(3, 640)     # 3 height frame id, 640 size of height
cap.set(4, 1080)    # 4 width frame id, 1080 width size
cap.set(10, 10)    # 10 brightness id

# Video is a sequence of images, so we need to read it as while loop.
while True:
    success, img = cap.read()   # success is boolean variable, img is a image variable
    cv.imshow("WebCam", img)

    if cv.waitKey(1) & 0xFF == ord('q'):   # Press key q to exit
        break