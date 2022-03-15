import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(512,512),(255,25,255),6)

cv.rectangle(img,(200,450),(300,370),(255,123,44))
font = cv.FONT_ITALIC
cv.putText(img,"sravya",(30,218),font,4,(12,33,55),thickness=4)

cv.imshow("image",img)
cv.waitKey(0)