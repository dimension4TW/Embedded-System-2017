from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(2)
camera.capture(rawCapture, format="bgr");
image = rawCapture.array

cv2.circle(image,(50,50),10,(255,0,0),2)
cv2.rectangle(image,(20,20),(60,60),(0,0,255),3)

#cv2.imshow("Fuck You",image)
cv2.imwrite("result_p1.jpg",image)
cv2.waitKey(0)
