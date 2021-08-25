
import matplotlib.pyplot as plt
import cv2
import numpy as np
import easyocr
import time
from pylab import rcParams
from IPython.display import Image
# rcParams['figure.figsize'] = 8, 16
reader = easyocr.Reader(['en'])
Image(r'L:\textDetection-Recognition\image2.jpg')
start = time.time()
cap = cv2.VideoCapture(0)
while True:

    ret, img = cap.read()
    cap = np.array(cap)
    output = reader.readtext(cap)
    print(output)
    cord = output[-1][0]

    x_min, y_min = [int(min(idx)) for idx in zip(*cord)]

    x_max, y_max = [int(max(idx)) for idx in zip(*cord)]

    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
    cv2.imshow("img", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(1) or 0xFF == ord('q'):
        break
end = time.time()
print("total time is :", end-start)
cap.release()
cv2.destroyAllWindows()
