import numpy as np
import cv2
img = cv2.imread(r"Smart-Text-Reader\test2.png")
h, w, c = img.shape
#img = cv2.resize(img,(h//2,w//2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshM = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)
threshG = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 5)

contours, hierarchy = cv2.findContours(
    threshG, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
imgc = img.copy()
cv2.drawContours(imgc, contours=contours, contourIdx=-1,
                 color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
print(contours)
cv2.imshow("opp", threshG)
cv2.imshow("op", imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()
