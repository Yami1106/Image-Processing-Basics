import cv2

rgb_img = cv2.imread('image.jpg')

hsv_img = cv2.cvtColor(rgb_img,cv2.COLOR_BGR2HSV)

print('image shape = ',hsv_img.shape)

cv2.imshow('original color image',rgb_img)
cv2.imshow('HSV image',hsv_img)

cv2.waitKey(0)
cv2.destroyAllWindows()