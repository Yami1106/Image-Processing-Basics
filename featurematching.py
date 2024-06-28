import cv2
import numpy as np

query_img=cv2.imread("image.jpg")
train_img=cv2.imread("savedImage.jpg")

query_img_bw=cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
train_img_bw=cv2.cvtColor(train_img,cv2.COLOR_BGR2GRAY)

orb=cv2.ORB_create()

queryKeyPoints,queryDescriptors = orb.detectAndCompute(query_img_bw,None)
trainKeyPoints,trainDescriptors = orb.detectAndCompute(train_img_bw,None)


matcher=cv2.BFMatcher()
matches = matcher.match(queryDescriptors,trainDescriptors)

final_img = cv2.drawMatches(query_img,queryKeyPoints,train_img,trainKeyPoints,matches[:20],None)

final_img=cv2.resize(final_img,(1000,650))

cv2.imshow("Matches",final_img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()