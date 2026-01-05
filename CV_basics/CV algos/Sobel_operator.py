import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("image.jpg")

g_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

g_double = g_img.astype(np.float64)

sc_mask = np.array([[-1,-2,-1],
                    [0,0,0],
                    [1,2,1]])

kx = cv.filter2D(g_double,ddepth=-1,kernel=sc_mask) #horizontal edges
ky = cv.filter2D(g_double,ddepth=-1,kernel=sc_mask.T) #vertical edges

#gradient magnitude
ked = np.sqrt(kx**2+ky**2)

plt.figure(figsize=(12,8))

plt.subplot(2, 2, 1)
plt.title("Grayscale")
plt.imshow(g_img, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.title("Horizontal Edges")
plt.imshow(np.abs(kx), cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.title("Vertical Edges")
plt.imshow(np.abs(ky), cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.title("Combined kx and ky")
plt.imshow(np.abs(ked), cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()

