import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if ret == True:
        img = frame
        img = cv2.resize(img, (512, 512))

        text = pytesseract.image_to_string(img)
        cv2.imshow('rame', img)
        print(text)

        
    else:
        break

cap.release()
cv2.destroyAllWindows()
