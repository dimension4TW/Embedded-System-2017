from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import RPi.GPIO as GPIO
import sys, Adafruit_DHT

sensor_args = {'11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302}
                
sensor = sensor_args['11']
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
    image = cv2.imread('image.jpg')
    if temperature > 30:
        face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        face_pos = face.detectMultiScale(gray, 1.1, 5)
        for (x,y,w,h) in face_pos:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,2,2),2)
    cv2.imshow('result',image)
    cv2.waitKey(0)
    
