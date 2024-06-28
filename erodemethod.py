#Syntax: cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])

import cv2
import numpy as np

image= cv2.imread('image.jpg')

window_name='Image'
kernal=np.ones((5,5),np.uint8)

image=cv2.erode(image,kernal)

cv2.imshow(window_name,image)

cv2.waitKey(0)
