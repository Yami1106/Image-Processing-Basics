#Syntax:  cv2.subtract(src1, src2)
import cv2
import numpy as np

image1=cv2.imread('image3.jpg')
image2=cv2.imread('image4.jpg')

sub=cv2.subtract(image1,image2)

cv2.imshow("Subtracted image",sub)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()