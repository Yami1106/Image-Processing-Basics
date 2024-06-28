#cv2.bitwise_xor(source1, source2, destination, mask)
import cv2
import numpy as np

img1=cv2.imread("image5.jpg")
img2=cv2.imread("image6.jpg")

dest_xor = cv2.bitwise_xor(img2,img1,mask= None)

cv2.imshow('Bitwise XOR',dest_xor)

cv2.waitKey(0)
cv2.destroyAllWindows