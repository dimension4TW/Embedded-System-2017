import cv2
import numpy as np

img = cv2.imread('2cat.jpg')

r, c, d = img.shape




#divde
bcat = img[0:r-1, 0:int(c/2) ]
wcat = img[0:r-1, int(c/2):c-1]

#turn into gray
wcat = cv2.cvtColor(wcat,cv2.COLOR_BGR2GRAY)

cv2.imshow("Origin", img) 
cv2.imshow("Black cat", bcat) 
cv2.imshow("White cat", wcat)
cv2.imwrite("black_cat.jpg",bcat)
cv2.imwrite("white_cat.png",wcat)
cv2.waitKey (0)
cv2.destroyAllWindows()



