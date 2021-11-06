import cv2
import numpy as np
import pytesseract
import pyttsx3
from deskew import deskew

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from scipy import stats
k1 = np.ones((3,17))
k2 = np.ones((5,5))

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate-50)
    engine.say(text)  
 
    engine.runAndWait()





page = []
img = cv2.imread(r"D:\final_year_project\Smart-Text-Reader\test3.jpeg")
img1=img.copy()
w,h,_ = img.shape

img = deskew(img)
lPage = img[0:w,0:h//2]
rPage = img[0:w,(h//2):h]

page=[lPage,rPage]
for i in page :

    #img = cv2.resize(img, (int(h//1.5),int(w//1.5)))
    imgg = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    img1 = np.array(255*(imgg/255)**1.7, dtype='uint8')

    mean = np.mean(np.array(img1))
    median = np.median(np.array(img1))
    print(mean, median)
    imgb = cv2.GaussianBlur(img1, (3,3),0)
    canny = cv2.Canny(imgb, 70, 25,apertureSize=3, L2gradient=True)
    imgdi = cv2.dilate(canny, k1, iterations=1)
    imger = cv2.erode(imgdi, k2, iterations=1)

    imgM = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,15,19)
    gg=cv2.resize(imgM,None,fx=0.7,fy=0.7)

    text = pytesseract.image_to_string(imgM)

    text = text.replace("\n"," ")
    if ", " in text:
        text=text.replace(", ",",")
    print(text)



    speak(text)
cv2.waitKey(0)
cv2.destroyAllWindows()