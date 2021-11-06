  
import numpy as np
import cv2

img = cv2.imread(r"D:\final_year_project\Smart-Text-Reader\test1.jpg")
kernal = np.ones((7, 2))


def applyHE(img):
    img = cv2.convertScaleAbs(img, alpha=1.3, beta=5)
    clahe = cv2.createCLAHE(clipLimit=1, tileGridSize=(8, 8))
    [b, g, r] = cv2.split(img)
    b = clahe.apply(b)
    g = clahe.apply(g)
    r = clahe.apply(r)
    nimg = cv2.merge([b, g, r])
    return nimg


imgah = applyHE(img)





def proprocess(img, kernal):

    imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgb = cv2.medianBlur(imgg, 3)
    canny = cv2.Canny(imgb, 10, 50)

    imgdi = cv2.dilate(canny, kernal, iterations=1)
    imger = cv2.erode(imgdi, kernal, iterations=1)
    return imger

def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)

        if area > 1000:
            peri = cv2.arcLength(i, True)

            approx = cv2.approxPolyDP(i, 0.02*peri, True)

            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area

    return biggest, max_area


def reorder(cpoints):
    cpoints = cpoints.reshape((4, 2))
    cpointsn = np.zeros((4, 1, 2), dtype=np.int32)
    add = cpoints.sum(1)

    cpointsn[0] = cpoints[np.argmin(add)]
    cpointsn[3] = cpoints[np.argmax(add)]
    diff = np.diff(cpoints, axis=1)
    cpointsn[1] = cpoints[np.argmin(diff)]
    cpointsn[2] = cpoints[np.argmax(diff)]

    return cpointsn


def pageDetect(img, kernal):
    img = cv2.resize(img, (720,640))
    h, w = img.shape[:2]
    imgC = img.copy()
    imger = proprocess(img, kernal)
    contours, hierarchy = cv2.findContours(
        imger, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    biggest, maxArea = biggestContour(contours)
    if biggest.size != 0:
        biggest = reorder(biggest)
        cv2.drawContours(imgC, biggest, -1, (0, 255, 0), 3)
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgCol = cv2.warpPerspective(imgah, matrix, (w, h),flags=cv2.INTER_CUBIC)
        return imgCol


imgCol = pageDetect(img, kernal,)

cv2.imshow("img", imgCol)
#cv2.imshow("imgb", img)
cv2.waitKey(0)

cv2.destroyAllWindows()