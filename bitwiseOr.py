#cv2.bitwise_or(source1, source2, destination, mask)
mport cv2
import numpy as np

img1=cv2.imread("image5.jpg")
img2=cv2.imread("image6.jpg")

dest_or = cv2.bitwise_or(img2,img1,mask= None)

cv2.imshow('Bitwise OR',dest_or)

cv2.waitKey(0)
cv2.destroyAllWindows