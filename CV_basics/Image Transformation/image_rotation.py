import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')

rows,col,ch = img.shape

mat = np.float32([[1,0,70],  
                  [0,1,50]]) 

# getRotationMatrix2D params (center,angle,scale)
# rotate by the center of the image hence col/2 and ros/2 by an angle of 45 degrees and shrink by 30%
#output of getRotationMatrix2D : 

#Matrix = [[scale*cosa    scale*sina  (1-scale*cosa)*cx-scale*sina*cy
#           -scale*sina   scale*cosa  scale*sina*cx+(1-scale*cosa)*cy ]]


dist = cv.warpAffine(img,cv.getRotationMatrix2D((col/2,rows/2),45,0.7),(col,rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')

plt.subplot(122)
plt.imshow(dist)
plt.title('Output')

plt.show()