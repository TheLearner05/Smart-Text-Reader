import numpy as np
import cv2
img = cv2.imread(r"L:\final_year_project\Smart-Text-Reader\test6.PNG")
h, w, c = img.shape
img = cv2.resize(img, (512, 512))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshM = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 5)
threshG = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 55, 5)


ele = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

di = cv2.morphologyEx(threshG, cv2.MORPH_DILATE, ele)
di1 = cv2.morphologyEx(threshG, cv2.MORPH_ERODE, ele)
cv2.imshow("di", di)
cv2.imshow("di1", di1)


#cannyop = cv2.Canny(threshG,100,150,)
#
contours, hierarchy = cv2.findContours(
    di, mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)
imgc = img.copy()


# print(cc,a)
cv2.drawContours(imgc, contours=contours, contourIdx=-100,
                 color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA, maxLevel=0)

cv2.imshow("cannyop", imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()
