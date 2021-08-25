
import pytesseract
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = cv2.imread(r'L:\final_year_project\test2.PNG', 0)
img = cv2.resize(img, (320, 480))
h,w = img.shape

sr,sc = int(0), int(0)
er,ec= int(h/2),int(w)
himg = img[sr:er,sc:ec]
#img =cv2.pyrUp(img)
img = cv2.convertScaleAbs(himg,  alpha=255/img.max(), beta=5)

imgeq = cv2.equalizeHist(img)
cl = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
imgcl = cl.apply(img)
op = np.hstack((img, imgcl))
text = pytesseract.image_to_string(imgcl)
cv2.imshow('rame', op)
print(text)
#ret,imgcl = cv2.threshold(img,10,255,cv2.THRESH_BINARY)

cv2.waitKey(0)
"""
while(True):
    ret, frame = cap.read()
    if ret == True:
        img = frame
        img = cv2.resize(img, (512,512))


        text = pytesseract.image_to_string(img)
        cv2.imshow('rame',img)
        print(text)

        if cv2.waitKey(3000):
			ans = input("do u want to go to next page")
			if ans == "yes":

    else:
        break
cap.release()
"""

cv2.destroyAllWindows()
