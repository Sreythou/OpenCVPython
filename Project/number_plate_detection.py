import cv2 as cv

frameWidth = 640
frameHeight = 400
minArea = 500
nPlateCascade = cv.CascadeClassifier("../haarcascades/haarcascade_russian_plate_number.xml")
color = (250, 250, 50)
count = 0

cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    success, img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv.putText(img, "Number Plate", (x, y - 5), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv.imshow("Roi", imgRoi)
    cv.imshow("Result", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.imwrite("../Resources/Scanned/NoPlat_" + str(count)+".jpg", imgRoi)
        cv.rectangle(img, (0, 200), (600, 300), (0, 255, 0), cv.FILLED)
        cv.putText(img, "Scan Saved", (150, 265), cv.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
        cv.imshow("Result", img)
        cv.waitKey(5000)
        count += 1
