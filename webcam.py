import cv2 as cv
cap = cv.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv.imshow("web",frame)
    if not ret:
        print("ss")
        break
    #cv.waitKey(1)
    if cv.waitKey(1) == ord("s"):
        break