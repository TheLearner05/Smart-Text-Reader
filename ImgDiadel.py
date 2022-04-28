
import cv2
import numpy as np
#from deskew import deskew
#from img_light import light_control

class ImgDiadel():
    
    def __init__(self):
        pass
    def Diadel(self,image):
        limg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


        limg = cv2.cvtColor(limg, cv2.COLOR_BGR2GRAY)

        k1 = np.ones((1, 15))
        #k2 = np.ones((2, 2))
        closing = cv2.morphologyEx(limg, cv2.MORPH_CLOSE, k1)
        clahe = cv2.createCLAHE(clipLimit=5, tileGridSize=(7, 7))
        closing = clahe.apply(closing)


    #cv2.imshow("closing", cv2.resize(closing, None, fx=0.6, fy=0.6))
        ret, thresh = cv2.threshold(closing, 40, 250, cv2.THRESH_OTSU)
    #thresh = cv2.dilate(thresh,k2)
    #cv2.imshow("thresh", cv2.resize(thresh, None, fx=0.6, fy=0.6))
        _,contours2,_ = cv2.findContours(thresh, mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)
        cnt = sorted(contours2, key=cv2.contourArea, reverse=True)
        for i in cnt:
            if 8000 < cv2.contourArea(i) < 100000:
                (x, y, w, h) = cv2.boundingRect(i)

            # print(cv2.contourArea(i))

                cv2.rectangle(image, (x, y), (x+w-1, y+h), (240, 240, 240), -1)
    #cv2.imshow("blacskhaat", cv2.resize(image, None, fx=0.6, fy=0.6))

        return image

