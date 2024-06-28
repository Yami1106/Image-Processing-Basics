#syntax: imread(widnow_name,image)

import cv2
path="/home/yami/Documents/pythonopencv/image.jpg"
#Reads image in default mode
image=cv2.imread(path)

#Reads image in grayscale mode
image2=cv2.imread(path,0)
window_name='image'

cv2.imshow(window_name,image)
cv2.imshow('grayscale',image2)

cv2.waitKey(0)
cv2.destroyAllWindows()