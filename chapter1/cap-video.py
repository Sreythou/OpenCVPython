import cv2 as cv

cap = cv.VideoCapture("../Resources/all_over.mp4")  # read video

# Video is a sequence of images, so we need to read it as while loop.
while True:
    success, img = cap.read()   # success is boolean variable, img is a image variable
    cv.imshow("All Over Video", img)

    if cv.waitKey(1) & 0xFF == ord('q'):   # Press key q to exit
        break