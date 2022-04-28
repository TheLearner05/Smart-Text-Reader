from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import time


class CaptureImage:
    def __init__(self):
        self.camera = PiCamera()
        #self.camera.resolution = (1024, 768)
        #self.camera.brightness = 50

    def CapImg(self):
        RawCapture = PiRGBArray(self.camera)
        time.sleep(0.1)
        self.camera.capture(RawCapture, format="bgr")
        self.image = RawCapture.array
        cv2.imwrite(
            '/home/pi/Desktop/STR_VR2/STR_VR2/images/test6.jpeg', self.image)
        # cv2.imshow("image",self.image)
        # cv2.waitKey(0)
        # RawCapture.close()
        # self.camera.close()
        return self.image
        # cv2.imshow("image",self.image)
        # cv2.waitKey(0)
