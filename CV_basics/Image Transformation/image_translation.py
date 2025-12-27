import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')

rows,col,ch = img.shape

mat = np.float32([[1,0,70],  # for x coordinate transforms(scale,shear,translation)
                  [0,1,50]]) #for y coordinate transforms(shear,scale,translation)

# input imgae, matrix, crop by (col,row)
dist = cv.warpAffine(img,mat,(col,rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')

plt.subplot(122)
plt.imshow(dist)
plt.title('Output')

plt.show()



