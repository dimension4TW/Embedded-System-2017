import requests
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


url =  'https://embedded-9d55.restdb.io/rest/rpi'
url2 = 'https://embedded-9d55.restdb.io/rest/rpi/5922902ca16aad7100000a0e'
url3 = 'https://embedded-9d55.restdb.io/rest/rpi/59229079a16aad7100000a12'



headers = {
    'content-type': 'application/json',
    'x-apikey':'e0e3cee33f6064e5c146bc2288c0e9c82bf1e',
    'cache-control':'no-cache'

}

re = requests.request('GET','https://embedded-9d55.restdb.io/rest/rpi',headers=headers)
print(re.text)

camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.capture(rawCapture, format='bgr')
image = rawCapture.array

"""
re = requests.put(url2, data="{'camera':'done'}",headers=headers)
print(re.text)
"""

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face_pos = face.detectMultiScale(gray, 1.1, 5)
for (x,y,w,h) in face_pos:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,2,2),2)

if len(face_pos) == 0:
    re = requests.put(url3, data="{\"status\":\"no\"}",headers=headers)
else:    
    re = requests.put(url3, data="{\"status\":\"yes\"}",headers=headers)
    
print(re.text)

cv2.imshow('lab10',image)
cv2.waitKey(0)

