import numpy as np
import cv2
from numpy.lib.type_check import imag

img = cv2.imread(r"L:\final_year_project\Smart-Text-Reader\test2.png")
img1 = cv2.imread(r"L:\final_year_project\Smart-Text-Reader\test1.png")
h, w, c = img.shape
img = cv2.resize(img, (h//2, w//2))
"""
per = 25
orb = cv2.ORB_create(1000)
kp1, des1 = orb.detectAndCompute(img1,None)
#imgkp1 = cv2.drawKeypoints(img,kp1,None)
kp2, des2 = orb.detectAndCompute(img,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.match(des2,des1)
matches.sort(key=lambda x:x.distance)
good  = matches[:int(len(matches)*(per/100))]
imgmatch = cv2.drawMatches(img,kp2,img1,kp1,good[:3],None,flags=2)

srcPoints = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1,1,2)
dstPoints = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1,1,2)

m,_ = cv2.findHomography(srcPoints, dstPoints,cv2.RANSAC, 5.0)


imgScan = cv2.warpPerspective(img,m,(w,h))
cv2.imshow("op",imgScan)

"""
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]

if angle < -45:
    angle = -(90 + angle)
else:
    angle = 0
print(angle)
h, w, c = img.shape

center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(
    img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
cv2.putText(rotated, "Angle: {:.2f} degrees".format(
    angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

print("[INFO] angle: {:.3f}".format(angle))
cv2.imshow("Input", img)
cv2.imshow("Rotated", rotated)


cv2.waitKey(0)

cv2.destroyAllWindows()
