import numpy as np
import cv2

img = cv2.imread(r"L:\final_year_project\test1.PNG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]

if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle


print(coords)
print(angle)
cv2.imshow("op", thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()
