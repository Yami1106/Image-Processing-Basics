#cv2.bitwise_and(source1, source2, destination, mask)

import cv2
import numpy as np

img1=cv2.imread('image5.jpg')
img2=cv2.imread('image6.jpg')

dest_and=cv2.bitwise_and(img2,img1,mask=None)

cv2.imshow('Bitwise And',dest_and)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()