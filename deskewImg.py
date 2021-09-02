import numpy as np
import cv2
from numpy.lib.type_check import imag

img = cv2.imread(r"L:\final_year_project\Smart-Text-Reader\test5.png")
imgc = img.copy()
imgg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
h, w = imgg.shape

bimg = cv2.medianBlur(imgg,3)

threshG = cv2.adaptiveThreshold(bimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,5)

ele = cv2.getStructuringElement(cv2.MORPH_RECT, (21,2))
dilate = cv2.dilate(threshG,ele)
cv2.imshow("dilate",dilate)

contours,hierarchy = cv2.findContours(dilate,mode=cv2.RETR_CCOMP,method=cv2.CHAIN_APPROX_NONE)
contours = sorted(contours,key=cv2.contourArea,reverse=True)

cv2.drawContours(imgc, contours=contours, contourIdx=-1,
                 color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA )

cv2.imshow("cc",imgc)

largestContour = contours[0]
middleContour = contours[len(contours) // 2]
smallestContour = contours[-1]
angle = sum([cv2.minAreaRect(largestContour)[-1], cv2.minAreaRect(middleContour)[-1], cv2.minAreaRect(smallestContour)[-1]]) / 3

center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(
    img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


cv2.imshow("threshG",rotated)




'''
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

coords = np.column_stack(np.where(thresh > 0))
print(coords[0])
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
cv2.imshow("Rotated", rotated)'''

cv2.waitKey(0)

cv2.destroyAllWindows()
