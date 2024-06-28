#syntax: waitkey([delay]), delay is in milliseconds and 0 is a special value which means forever
#syntax: destroyAllWindows(winname), if left blank destroys all the opened windows and deallocates the associated memory usage for all the windows
import cv2

img=cv2.imread("image.jpg",cv2.IMREAD_COLOR)

cv2.imshow("image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()