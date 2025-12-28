import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')

rows,cols,ch =img.shape

img_shrink = cv.resize(img,(100,100),interpolation=cv.INTER_AREA)
img_enlarged = cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)

plt.subplot(131)
plt.imshow(img)
plt.title('Input')

plt.subplot(132)
plt.imshow(img_shrink)
plt.title('Shrunken image')

plt.subplot(133)
plt.imshow(img_enlarged)
plt.title('Enlarged image')

plt.show()