import os
import RPi.GPIO as go
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import requests
import time
import sys
import signal

# mode1: secure
# mode2: killing
v = 343  # 331 + 0.6 * 20
trigger_pin = 16
echo_pin    = 18


def front(t):
    go.output(7, False)
    go.output(11,True)
    go.output(13,True)
    go.output(15,False)
    time.sleep(t)
    go.output(7, False)
    go.output(11,False)
    go.output(13,False)
    go.output(15,False)

def rear(t):
    go.output(7, True)
    go.output(11,False)
    go.output(13,False)
    go.output(15,True)
    time.sleep(t)
    go.output(7, False)
    go.output(11,False)
    go.output(13,False)
    go.output(15,False)
    
def left(t):
    go.output(7, True)
    go.output(11,False)
    go.output(13,True)
    go.output(15,False)
    time.sleep(t)
    go.output(7, False)
    go.output(11,False)
    go.output(13,False)
    go.output(15,False)
    
def right(t):
    go.output(7, False)
    go.output(11,True)
    go.output(13,False)
    go.output(15,True)
    time.sleep(t)
    go.output(7, False)
    go.output(11,False)
    go.output(13,False)
    go.output(15,False)
    
def measure():
    go.output(trigger_pin, go.HIGH)
    time.sleep(0.00001)
    go.output(trigger_pin, go.LOW)
    while go.input(echo_pin) == go.LOW:
        pulse_start = time.time()
    while go.input(echo_pin) == go.HIGH:
        pulse_end   = time.time()
    t = pulse_end - pulse_start
    d = (t * v) / 2
    return d * 100

def secure():
    go.setmode(go.BOARD)
    # for distance detector
    go.setup(trigger_pin, go.OUT)
    go.setup(echo_pin, go.IN)
    # for car's movement
    go.setup(7,  go.OUT)
    go.setup(11, go.OUT)
    go.setup(13, go.OUT)
    go.setup(15, go.OUT)
    time.sleep(2)
    
    global interrupt
    try:
        pid = os.fork()
        if pid == 0: # child process
            count = 0
            camera = PiCamera()
            camera.resolution = (320, 240)
            camera.framerate = 32
            rawCapture = PiRGBArray(camera, size=(320,240))
            time.sleep(2)
            for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
                flag = 1
                image = frame.array
                face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                face_pos = face.detectMultiScale(gray, 1.1, 5)
                for (x,y,w,h) in face_pos:
                    cv2.rectangle(image,(x,y),(x+w,y+h),(255,2,2),2)
                    count = count + 1
                    flag = 0
                if count == 10:
                    # send server picture first
                    # active beep for 5 seconds
                    count = 0
                if flag:
                    count = 0
                cv2.waitKey(1) & 0xFF
                rawCapture.truncate(0)
                cv2.imshow('result',image)
                
        else:
            while True:
                f2 = open('int.txt', 'r')
                temp2 = f2.read(1)
                f2.close()
                if measure() < 20:
                    left(0.5)
                else:
                    front(0.5)
                if temp2=='1':
                    os.kill(pid, signal.SIGKILL)
                    break
    except OSError:
        print ("secure fork error")
    go.cleanup()
    sys.exit(0)

    
while True:
    print('GG')
    global interrupt
    interrupt = 0
    mode = 'secure'
    file = open('int.txt', 'w')
    file.write('0')
    file.close()
    
    try:
        if mode == 'secure':
            ppid = os.fork()
        else:
            ppid = 1
        if ppid == 0: # child process
            # receive mode
            if mode == 'secure':
                print('a')
                time.sleep(4)
                secure()
                print('b')
        else: # parent process
            while True:
                r = requests.get('http://localhost:8888')
                print(r.text)
                if mode == 'secure':
                    if r.text == 'mode2':
                        file = open('int.txt', 'w')
                        file.write('1')
                        file.close()
                        mode = 'killing'
                        status1 = os.wait()
                else:
                    if r.text == 'mode1':
                        break
    except OSError:
        print ("main fork error")


        
'''  
def killing():
    while True:
        r = requests.get(url, params=payload)
        if payload == 'w':
            front(0.5)
        elif payload == 'a':
            left(0.5)
        elif payload == 'd':
            right(0.5)
        elif payload == 's':
            rear(0.5)
        elif payload == 'q':
            sys.exit(0)
'''
    
    
