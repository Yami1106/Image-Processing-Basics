#syntax: imwrite(filename,image)
#imwrite is a method used to save an image to any storage device

import cv2
import os


image_path=r"/home/yami/Documents/pythonopencv/image.jpg"
directory=r"/home/yami/Documents/pythonopencv"


img=cv2.imread(image_path)

os.chdir(directory)

print("Before saving image:")
print(os.listdir(directory))
filename='savedImage.jpg'
cv2.imwrite(filename,img)

print('After saving image:')

print(os.listdir(directory))

print("Successfully saved")

