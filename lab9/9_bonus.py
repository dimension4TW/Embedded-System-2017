import cv2  
import numpy as np    
   
 
img = cv2.imread("cat_sa.jpg")  
median = cv2.medianBlur(img,5)
  
cv2.imshow("Salt", img)  
cv2.imshow("Median", median)  
  
cv2.waitKey(0)
