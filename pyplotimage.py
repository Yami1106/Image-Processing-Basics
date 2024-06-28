#matplot uses BGR color format hece the colors in the output come inverted 

import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("image.jpg")

plt.imshow(img)

plt.waitforbuttonpress()
plt.close('all')