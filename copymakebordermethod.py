#Syntax: cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)

import cv2
image=cv2.imread('image.jpg')

window_name="Image"

imag=cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,None,value=0)
image2=cv2.copyMakeBorder(image,100,100,50,50,cv2.BORDER_REFLECT)
cv2.imshow(window_name,imag)
cv2.waitKey(0)

cv2.imshow(window_name,image2)
cv2.waitKey(0)

cv2.destroyAllWindows()