#Syntax: cv2.bitwise_not(source, destination, mask)
import cv2
import numpy as np

img1=cv2.imread("image5.jpg")
img2=cv2.imread("image6.jpg")

dest_not1 = cv2.bitwise_not(img1,mask= None)
dest_not2 = cv2.bitwise_not(img2,mask= None)

cv2.imshow('Bitwise NOT on image1',dest_not1)
cv2.imshow('Bitwise NOT on image2',dest_not2)

cv2.waitKey(0)
cv2.destroyAllWindows