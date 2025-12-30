import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')

cropped_img =img[100:250,100:250]

plt.subplot(121)
plt.imshow(img)
plt.title('Input')

plt.subplot(122)
plt.imshow(cropped_img)
plt.title('Output')

plt.show()