import numpy as np
import cv2

img = cv2.imread(r"Smart-Text-Reader\test6.PNG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (512, 512))
h, w = img.shape

corners = cv2.goodFeaturesToTrack(img, 200, 0.1, 80,)
print(corners)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

#op = np.hstack((img, thimg))
cv2.imshow("img", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
