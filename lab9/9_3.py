import cv2
import numpy as np

img_origin = cv2.imread("building.jpg",0);  
img = img_origin

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
abs_sobelx = cv2.convertScaleAbs(sobelx)
abs_sobely = cv2.convertScaleAbs(sobely)

img_temp = cv2.addWeighted(abs_sobelx,0.5,abs_sobely,0.5,0);

cv2.imshow("Sobel", img_temp)
cv2.imwrite("Sobel.jpg",img_temp)
cv2.waitKey(0)  
cv2.destroyAllWindows()



 
  
  

