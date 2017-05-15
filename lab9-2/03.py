from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320,240))

time.sleep(2)

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    image = frame.array
    image = cv2.imread('image.jpg')
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face_pos = face.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in face_pos:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,2,2),2)
    cv2.imshow('result',image)
    cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q");
    break