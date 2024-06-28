#Syntax: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)

import cv2
import numpy as np 

image1=cv2.imread('image1.jpg')
image2=cv2.imread('image2.jpg')

weightedSum=cv2.addWeighted(image1,0.5,image2,0.4,0)

cv2.imshow('weighted image',weightedSum)


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()