import cv2
import numpy as np
from scipy import stats
import pytesseract
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

k1 = np.ones((3, 17))
k2 = np.ones((3, 3))

img = cv2.imread(r"D:\final_year_project\Smart-Text-Reader\test3.jpeg")

imgc = img.copy()
h,w ,_ = img.shape
lPage = img[0:h,0:w//2]
rPage = img[0:h,(w//2)-3:w]







gray_pg = cv2.cvtColor(lPage, cv2.COLOR_BGR2GRAY)
contrast_pg = np.array(255*(gray_pg/255)**1.2, dtype='uint8')

def set(contrast_pg,factor):
    mean = np.mean(np.array(contrast_pg))
    median = np.median(np.array(contrast_pg))
    if mean < 75 and median <100 :
        contrast_pg = np.array(255*(gray_pg/255)**, dtype='uint8')
        set(contrast_pg)

    return mean, median

mean , median = set(contrast_pg)
print(mean,median)
cv2.imshow("contrast_pg",contrast_pg)
blurred_pg = cv2.GaussianBlur(contrast_pg, (3, 3), 0)
canny_pg = cv2.Canny(blurred_pg, 70, 25, apertureSize=3, L2gradient=True)
cv2.imshow("canny_pg",canny_pg)
dilated_pg = cv2.dilate(canny_pg, k1, iterations=1)
eroded_pg = cv2.erode(dilated_pg, k2, iterations=1)
cv2.imshow("eroded_pg",eroded_pg)
    
contours, hierarchy = cv2.findContours(
    eroded_pg, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

# contours = sorted(contours,key=cv2.contourArea,reverse=True)
cnt = max(contours, key=cv2.contourArea)
#method 1
(x, y, w, h) = cv2.boundingRect(cnt)
#cv2.rectangle(imgc, (x, y), (x+w, y+h), (0, 0, 255), 2)

#mthod 2
rect = cv2.minAreaRect(cnt)

box = cv2.boxPoints(rect).astype('int')
print(box)
#method 3
hull = cv2.convexHull(cnt, clockwise=True)

#method 4
peri = cv2.arcLength(hull, True)
approx = cv2.approxPolyDP(hull, 0.035* peri, True)

output = lPage.copy()
	# draw the approximated contour on the image

cv2.drawContours(output, cnt, -1, (0, 255, 0), 3)
cv2.imshow("dfds",output)
print(len(hull))
#imgc = cv2.drawContours(imgc,[hull],-1,(0,0,255),2)
pts1 = np.float32(box)
pts2 = np.float32([[0, 0], [w, 0], [w, h], [0,h]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgCol = cv2.warpPerspective(imgc, matrix, (w, h),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REPLICATE)
H,W,_ = imgCol.shape


"""

imggl = cv2.cvtColor(rPage, cv2.COLOR_BGR2GRAY)
img1l = np.array(255*(imggl/255)**2, dtype='uint8')


imgbl = cv2.GaussianBlur(img1l, (3, 3), 0)
cannyl = cv2.Canny(imgbl, 27, 30, L2gradient=True)
imgdil = cv2.dilate(cannyl, k1, iterations=1)
imgerl = cv2.erode(imgdil, k2, iterations=1)


cv2.imshow("ss",lPage)





contours2, hierarchy = cv2.findContours(
    imgerl, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

cntl = max(contours2, key=cv2.contourArea)
rectl = cv2.minAreaRect(cnt)

boxl = cv2.boxPoints(rectl).astype('int')


hulll = cv2.convexHull(cntl, clockwise=True)
print(hulll)



#imgcl = cv2.drawContours(rPage,[hulll],-1,(0,0,255),2)


"""






cv2.waitKey(0)
cv2.destroyAllWindows()
