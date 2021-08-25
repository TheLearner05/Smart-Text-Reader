import numpy as np
import cv2

img = cv2.imread(r"L:\final_year_project\test2.PNG")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img.max(), img.min())
ret, thimg = cv2.threshold(img,120,255, cv2.THRESH_BINARY)
print(thimg.max(), thimg.min())
op = np.hstack((img, thimg))
cv2.imshow("img", op)
cv2.waitKey(0)

cv2.destroyAllWindows()
