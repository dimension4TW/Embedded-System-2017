import cv2
import numpy

image = cv2.imread('image.jpg')
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face_pos = face.detectMultiScale(gray, 1.1, 5)

for (x,y,w,h) in face_pos:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,2,2),2)
    
cv2.imshow('result',image)
cv2.imwrite('result.jpg',image)
