import cv2

path=r"image.jpg"
img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()