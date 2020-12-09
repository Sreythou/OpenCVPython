import cv2 as cv

def getContours(img):
    # Contours: curve joining all the continuous points
    _, contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)

        cv.drawContours(imgContour, cnt, -1, (255, 0, 0))
        arc = cv.arcLength(cnt, True)
        print(arc)

        approx = cv.approxPolyDP(cnt, 0.02 * arc, True)
        print(len(approx))  # Can know what the shape is

        objCor = len(approx)
        x, y, w, h = cv.boundingRect(approx)    # bounding rectangle


        if objCor == 3: objectType = "Triangle"
        elif objCor == 4:
            aspRatio = w/float(h)
            if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
            else: objectType = "Rectangle"
        elif objCor > 7: objectType = "Circle"
        else: objectType = "None"
        cv.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(imgContour, objectType, (x+5, y + (h//2)+10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

path = "../Resources/shape.jpg"
img = cv.imread(path)
imgContour = img.copy()

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)
getContours(imgCanny)

# cv.imshow("Original Image", img)
# cv.imshow("Gray Image", imgGray)
# cv.imshow("Blur Image", imgBlur)
# cv.imshow("Canny Image", imgCanny)
cv.imshow("Contours Image", imgContour)


cv.waitKey(0)
