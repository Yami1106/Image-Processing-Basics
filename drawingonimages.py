import numpy as np
import cv2

#Creating a black image with 3 channels RGB and unsigned int datatype
img=np.zeros((400,400,3),dtype="uint8")

cv2.rectangle(img,(30,30),(300,200),(0,255,0),5)
cv2.imshow('dark',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

