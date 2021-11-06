'''import cv2
import numpy as np
from skimage.transform import hough_line, hough_line_peaks
from skimage.transform import rotate
from scipy.stats import mode
img = cv2.imread(r'D:\final_year_project\Smart-Text-Reader\test7.jpg')
#img = cv2.resize(img,None, fx=0.6, fy=0.6)
def deskew(image):
    # convert to edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 150, 150, apertureSize=3)
    # Classic straight-line Hough transform between 0.1 - 180 degrees.
    tested_angles = np.deg2rad(np.arange(0.1, 180.0))
    h, theta, d = hough_line(edges, theta=tested_angles)

    # find line peaks and angles
    accum, angles, dists = hough_line_peaks(h, theta, d)

    # round the angles to 2 decimal places and find the most common angle.
    most_common_angle = mode(np.around(angles, decimals=2))[0]

    # convert the angle to degree for rotation.
    skew_angle = np.rad2deg(most_common_angle - np.pi/2)
    print(skew_angle)
    return skew_angle
gg=int(rotate(img, deskew(img)))
cv2.imshow("nimg", gg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import numpy as np
import cv2
import math
import imutils
angle=[]
def deskew(image):

    image = cv2.resize(image, None, fx=0.6, fy=0.6)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 200, 170, apertureSize=3)

    linesCoords = cv2.HoughLinesP(
        edges, 1, np.pi/180, 100, minLineLength=150, maxLineGap=5)
    
    for i in linesCoords:

        x1, y1, x2, y2 = i[0]

        angle.append(math.degrees(math.atan((y2-y1)/(x2-x1))))
    angle1=sorted(angle,reverse=True)
    print()    
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
    cv2.imshow("Result Image",cv2.resize(image,None,fx=0.7,fy=0.7))
    rotated = imutils.rotate_bound(image, -angle1[0])
    return rotated
img = cv2.imread(r"D:\final_year_project\Smart-Text-Reader\test8.jpg")

op = deskew(img)
cv2.imshow("op", op)
cv2.waitKey(0)
cv2.destroyAllWindows()

