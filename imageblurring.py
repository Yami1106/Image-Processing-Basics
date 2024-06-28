import cv2 
import numpy as np 
  
image = cv2.imread("/home/yami/Documents/pythonopencv/image1.jpg") 
  
cv2.imshow("Original Image", image) 

  
# Gaussian Blur 
Gaussian = cv2.GaussianBlur(image, (7, 7), 0) 
cv2.imshow("Gaussian Blurring", Gaussian)  
  
# Median Blur 
median = cv2.medianBlur(image, 5) 
cv2.imshow("Median Blurring", median) 
  
  
# Bilateral Blur 
bilateral = cv2.bilateralFilter(image, 9, 75, 75) 
cv2.imshow("Bilateral Blurring", bilateral)


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows() 