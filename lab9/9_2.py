import cv2
import numpy as np
img = cv2.imread('nctu.JPG')
img_logo = cv2.imread('NCTU_LOGO.png')

r1, c1, d1 = img.shape
r2, c2, d2 = img_logo.shape

M = cv2.getRotationMatrix2D((c2/2,r2/2),90,1)
dst = cv2.warpAffine(img_logo,M,(c2,r2))

dst = cv2.resize(dst, (200,200), interpolation = cv2.INTER_CUBIC)
image = np.zeros( (200,c1,3) , dtype = "uint8")
image[0:200, 0:200] = dst;
temp = img[140:340, 0:c1]
img = cv2.addWeighted(temp,0.6,image,0.4,30)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Image_g", img) 
cv2.imwrite("output.jpg",img)
cv2.waitKey (0)
cv2.destroyAllWindows()

