import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')
rows, cols,ch = img.shape


M = np.float32([[1,  0, 0], # x transforms
                [0, -1, rows],#y transforms
                [0,  0, 1]])# perspective (prespectives,prespectivey,normalization)
reflected_img_x = cv.warpPerspective(img, M,
                                   (int(cols),
                                    int(rows)))


M2 = np.float32([[-1,  0, cols],
                [0, 1, 0],
                [0,  0, 1]])
reflected_img_y = cv.warpPerspective(img, M2,
                                   (int(cols),
                                    int(rows)))


plt.subplot(131)
plt.imshow(img)
plt.title('Input')

plt.subplot(132)
plt.imshow(reflected_img_x)
plt.title('Outputx')

plt.subplot(133)
plt.imshow(reflected_img_y)
plt.title('Outputy')

plt.show()
