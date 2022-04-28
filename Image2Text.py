import pytesseract
import cv2
import numpy as np
from scipy import stats
from ImgDiadel import ImgDiadel
from ImgAdpTh import ImgAdpTh
from ImgText import ImgText
from SpellCheck import SpellCheck
#from ImageOri import ImageOri

class Image2Text:
    MyDiadelImg = ImgDiadel()
    MyAdpThImg = ImgAdpTh()
    MyTextImg = ImgText()
    MyCheckText = SpellCheck()
    #MyOrintImg = ImageOri()

    def __init__(self):
        pass
    def Convert2Text(self,CapImg):
        #self.DiadelImg = self.MyDiadelImg.Diadel(CapImg)
        self.AdpThImg = self.MyAdpThImg.AdpTh(CapImg)
       # self.GetDeskImg = self.MyOrintImg.GetDeskew(self.AdpThImg)
        self.text = self.MyTextImg.Text(self.AdpThImg)
        # print(text)
        #self.corr_text = self.MyCheckText.Checker(self.text)
        return self.text 

           