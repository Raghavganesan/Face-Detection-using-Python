#this is a face detection project which will detect any face movt

#there will be a rectangular box which will show green and red border


print()

import cv2
a = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
b = cv2.VideoCapture(0)  # gives access to the wwebcam
while True:
    c_rec,d_img = b.read()
    e = cv2.cvtColor(d_img,cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e,1.3,6)
    for (x1,y1,w1,h1) in f:
        cv2.rectangle(d_img,(x1,y1),(x1+w1,y1+h1),(255,0,0),5)
    cv2.imshow('img',d_img)
    h = cv2.waitKey(40) & 0xff
    if h ==40:
        break
b.release()
cv2.destroyAllWindows()