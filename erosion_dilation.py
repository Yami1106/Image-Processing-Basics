import cv2
import numpy as np

img = cv2.imread("image.jpg",0)

kernal=np.ones((5,5),np.uint8)

img_erosion=cv2.erode(img,kernal,iterations=1)
img_dilation=cv2.dilate(img,kernal,iterations=1)

cv2.imshow("Input",img)
cv2.imshow("Erosion",img_erosion)
cv2.imshow("Dilation",img_dilation)

if cv2.waitKey(0) & 0xff ==27:
    cv2.destroyAllWindows()