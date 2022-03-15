import cv2 as cv
cap = cv.VideoCapture("C:\Users\SRAVYAVANI\Downloads\Telegram Desktop\sravya.mp4")
while cap.isOpened():
    ret,frame = cap.read()
    cv.imshow("web",frame)
    if not ret:
        print("video error")
        break
    #cv.waitKey(1)
    if cv.waitKey(1) == ord("s"):
        break