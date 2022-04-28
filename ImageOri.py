import matplotlib.pyplot as plt
from PIL import Image
from Camera import CaptureImage
import numpy as np
import cv2
import math
import imutils
from ImgLightCol import ImgLightCol
from collections import Counter
angle = []


class ImageOri:
    MyLightColImg = ImgLightCol()

    def __init__(self):
        pass

    def Deskew(self, image):

        h, w, _ = image.shape
        # image = image[0:h, 250:w-250]
        self.LightImg = self.MyLightColImg.lightControl(image, 1.5)
        cv2.imwrite(
            "/home/pi/Desktop/STR_VR2/STR_VR2/images/ContrasImg6.jpg", self.LightImg)
        k1 = (np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]))/9

        gray = cv2.cvtColor(self.LightImg, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        edges = cv2.Canny(gray, 40, 110, apertureSize=3, L2gradient=True)
        edges = cv2.dilate(edges, np.ones((1, 15)))
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 180, 200)

        try:

            for i in lines:

                x1, y1, x2, y2 = i[0]
                ang = round(math.degrees(math.atan((y2-y1)/(x2-x1))), 3)

                if 80 > ang > -80:
                    # if ang <0:
                    # ang = -ang
                    angle.append(ang)

                    # cv2.line(self.LightImg, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    # cv2.im"/home/pi/Desktop/STR_VR2/STR_V2/images/LightImg7.jpg", self.LightImg)

            sAngle = sorted(angle, reverse=True)
            # cv2.imshow("asd", self.LightImg)
            # cv2.imwrite('/home/pi/Desktop/STR_V2/STR_V2/images/imgori.jpeg', self.LightImg)

            d = Counter(sAngle)

            sAngle = d.most_common()[0][0]

            # print(sAngle)

            if 0 > sAngle < -45:

                ang = -(90+sAngle)

            elif -45 < sAngle < 0:
                ang = -sAngle

            elif sAngle == 0:
                ang = sAngle

            elif 0 < sAngle < 45:
                ang = -sAngle

            elif 0 < sAngle > 45:
                ang = 90-sAngle
            ang = round(ang, 3)

            # print(ang)
            rotatedImg = imutils.rotate_bound(self.LightImg, ang)
            # length.append(np.sqrt((x2-x1)**2+ (y2-y1)**2))
            print("deskewed angle is :", ang)
            # cv2.imshow("gg", rotatedImg)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            cv2.imwrite(
                "/home/pi/Desktop/STR_VR2/STR_VR2/images/rotatedImg6.jpg", rotatedImg)
            return rotatedImg

        except:

            print("unable to find angle")
            # cv2.imshow("gg", self.LightImg)
            # cv2.waitKey(0)
            # cv2.destroyAllWindow()
            return self.LightImg
