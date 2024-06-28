import cv2
import numpy as np

img=cv2.imread("image.jpg")

(rows, cols)=img.shape[:2]

M=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)

res=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Image",res)

cv2.waitKey(0)
cv2.destroyAllWindows()