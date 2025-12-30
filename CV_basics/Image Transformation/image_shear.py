import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')

rows,cols,ch =img.shape

M=np.float32([[1.0,0.5,0],[0,1,0],[0,0,1]])
M2=np.float32([[1.0,0,0],[0.5,1,0],[0,0,1]])

# When an image is sheared, it expands beyond its original boundaries, A larger canvas to see the full sheared image is needed
shear_x=cv.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5))) 
shear_y=cv.warpPerspective(img,M2,(int(cols*1.5),int(rows*1.5))) 

plt.subplot(131)
plt.imshow(img)
plt.title('Input')

plt.subplot(132)
plt.imshow(shear_x)
plt.title('Shrunken image')

plt.subplot(133)
plt.imshow(shear_y)
plt.title('Enlarged image')

plt.show()