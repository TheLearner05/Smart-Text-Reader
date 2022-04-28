import time
import sys
import pandas as pd
import cv2
import numpy
import numpy as np
import RPi.GPIO as GPIO
from threading import Thread, Event, Timer
from Camera import CaptureImage
#from Image2Text import Image2Text
from Text2Speech import Text2Speech
from SetPWM import SetPWM
from UpdateSys import perpetualTimer
from ImageOri import ImageOri
#from ImgLayout import ImgLayout
#from ImgLayout import ImgLayout
#from ImgSplit import ImgSplit
#from Speech2Text import Speech2Text
from SoftSPI import SPIConfig
from tp import gcp_ocr
from tp import azure_tts
from testsp import Speech2txt


class Sys:
    MyCapture = CaptureImage()
    #MyText = Image2Text()
    MySpeak = Text2Speech()
    MyBright = SetPWM()
    MyOrintImg = ImageOri()
    #MyLayoutImg = ImgLayout()
    #MySplitImg = ImgSplit()
    #MySpeech = Speech2Text()
    MyAmbientVal = SPIConfig()
    MyInputLang = Speech2txt()
    gcp_ocr = gcp_ocr()
    azure_tts = azure_tts()

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.Button = 0
        # self.CurrentValue = 512
        self.OnesecCnt = perpetualTimer(1, self.UpdatePWM)
        self.CheckStatusFlag = True

    def Flow(self):
        g1 = time.perf_counter()
        print('Initializing')
        self.weltxt = "Hello. Welcome to this journey of learning with Smart Text Reader Please select the preferred language"
        self.MySpeak.Convert2Speech(self.weltxt, 'english')
        # self.MySpeak.Convert2Speech(self.weltxt)
        #self.Inputlang = self.MyInputLang.Sp2txt()
        self.Inputlang = input().capitalize()
        # self.MySpeak.Convert2Speech(self.Ptext, 'english')
        self.OnesecCnt.start()
        self.Ptext = 'press the button'
        print(self.Ptext)
        _Continue = True
        self.Button = GPIO.input(22)
        while _Continue:

            while not self.Button:
                self.Button = GPIO.input(22)

                if self.Button:
                    self.CheckStatusFlag = True
                    print('button pressed')
                    self.Button = 0
                    # self.MySpeech.talk2pi()
                    self.Snap = self.MyCapture.CapImg()
                    self.CheckStatusFlag = False
                    # self.CurrentThread = Thread(target = self.MySpeech.talk2pi)
                    # cv2.imshow('imgt',self.Snap)
                    # cv2.waitKey(0)
                    self.DeskImg = self.MyOrintImg.Deskew(self.Snap)

                    cv2.imwrite(
                        '/home/pi/Desktop/STR_VR2/STR_VR2/Deskimg.jpeg', self.DeskImg)
                    # MyText.Convert2Text(self.DeskImg)
                    self.Text, self.pageDetect = self.gcp_ocr.getResult(
                        path='/home/pi/Desktop/STR_VR2/STR_VR2/Deskimg.jpeg')
                    # print(self.Text)
                    g2 = time.perf_counter()
                    print(round(g2-g1, 3))
                    # self.MySpeak.Convert2Speech(self.Text, self.lang)
                    h, w, _ = self.DeskImg.shape
                    for i in self.pageDetect:
                        # print(i["x"])
                        i["x"] = i["x"]*w
                        i["y"] = i["y"]*h

                    (x1, y1) = (self.pageDetect[0]
                                ["x"], self.pageDetect[0]["y"])
                    wn = int(self.pageDetect[1]["x"] - self.pageDetect[0]["x"])
                    hn = int(self.pageDetect[2]["y"] - self.pageDetect[1]["y"])
                    (x2, y2) = (self.pageDetect[2]
                                ["x"], self.pageDetect[2]["y"])

                    if wn > 1.3*hn:
                        img1 = self.DeskImg[0:hn, int(
                            self.pageDetect[0]["x"]+1):int(self.pageDetect[0]["x"])+wn//2]
                        img2 = self.DeskImg[0:hn, int(
                            self.pageDetect[0]["x"])+wn//2 + 1:int(self.pageDetect[1]["x"])]
                        #cv2.imshow("ag", img1)
                        #cv2.imshow("gs", img2)
                        cv2.imwrite(
                            '/home/pi/Desktop/STR_VR2/STR_VR2/leimg.jpeg', img1)
                        cv2.imwrite(
                            '/home/pi/Desktop/STR_VR2/STR_VR2/reimg.jpeg', img2)
                        self.Ltext, _ = self.gcp_ocr.getResult(
                            path='/home/pi/Desktop/STR_VR2/STR_VR2/leimg.jpeg')
                        self.Rtext, _ = self.gcp_ocr.getResult(
                            path='/home/pi/Desktop/STR_VR2/STR_VR2/reimg.jpeg')
                        self.azure_tts.azure_tts_rest(
                            self.Ltext, self.Inputlang)
                        self.LComNtext = 'Left Page completed'
                        self.MySpeak.Convert2Speech(self.LComNtext, 'english')
                        self.azure_tts.azure_tts_rest(
                            self.Rtext, self.Inputlang)
                        self.RComNtext = 'Right Page completed'
                        self.MySpeak.Convert2Speech(self.RComNtext, 'english')
                        # cv2.imwrite()
                    else:

                        # print("singlepage")

                        self.azure_tts.azure_tts_rest(
                            self.Text, self.Inputlang)

                    print("page is Done")
                    self.Dtext = 'Page reading is completed'
                    self.MySpeak.Convert2Speech(self.Dtext, 'english')
                    # time.sleep(5)
                    self.Appclose = 0
                    self.Count = 0
                    self.PCount = 0
                    self.RNtext = 'Press button to read next page'
                    self.MySpeak.Convert2Speech(self.RNtext, 'english')
                    self.Button = GPIO.input(22)
                    while not self.Button:
                        self.Button = GPIO.input(22)
                        self.Count = self.Count + 1
                        #self.CheckCount = self.Count

                        # if self.Count > 10:
                        #self.PCount = self.PCount + 1
                        # print(self.Count)

                        time.sleep(0.1)
                    if self.Count > 100:  # 20 Sec Wait
                        _Continue = False
                        self.AppClose = 1
                        self.Button = 1

                    else:
                        #print("123456789")
                        self.Button = GPIO.input(22)
                        #_Continue = True

                    # print("Application Shutdown")

        if self.AppClose == 1:
            self.MyBright.endprogram()
            GPIO.cleanup()
            self.OnesecCnt.cancel()
            print("Application Terminated")

    def UpdatePWM(self):
        if self.CheckStatusFlag:
            self.CurrentValue = self.MyAmbientVal.AmbientLightVal()
            self.MyBright.led_brightness(self.CurrentValue)
        else:
            self.MyBright.led_brightness(0)
