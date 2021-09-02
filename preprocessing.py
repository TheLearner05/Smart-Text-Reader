import numpy as np
import cv2

img = cv2.imread(r"L:\final_year_project\Smart-Text-Reader\test3.png")
img = cv2.resize(img, (512, 512))
imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = imgg.shape
imgb = cv2.GaussianBlur(imgg, (5, 5), 1)
can = cv2.Canny(imgb, 10, 50)
kernal = np.ones((7, 2))
imgdi = cv2.dilate(can, kernal, iterations=1)
imger = cv2.erode(imgdi, kernal, iterations=1)

imgC = img.copy()

contours, hierarchy = cv2.findContours(
    imger, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=cv2.contourArea)
cv2.drawContours(imgC, contours[-1], -1, (0, 255, 0), 3)


def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        print(area)
        if area > 1000:
            peri = cv2.arcLength(i, True)
            print("peri",peri)
            approx = cv2.approxPolyDP(i, 0.02*peri, True)
            print("approc=x",approx)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
            print(biggest, max_area)
    return biggest, max_area


biggest, maxArea = biggestContour(contours)


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


if biggest.size != 0:
    biggest = reorder(biggest)
    cv2.drawContours(imgC, biggest, -1, (0, 255, 0), 3)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgCol = cv2.warpPerspective(img, matrix, (w, h))


print(biggest)
#op = np.hstack((img, thimg))
#cv2.imshow("img", imgCol)
cv2.imshow("imgb", imgC)
cv2.waitKey(0)

cv2.destroyAllWindows()
