#code to conver BGR to RGB color format

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("image.jpg")

RGB_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(RGB_img)
plt.waitforbuttonpress()
plt.close('all')