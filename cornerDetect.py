import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")
def nothing(x):
    pass
cv2.createTrackbar("quality", "frame",1,100,nothing)
while True:
    ret,frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    h,w = gray.shape
    quality = cv2.getTrackbarPos("quality","frame")
    quality = quality/100 if quality>0 else 0.01
    corners = cv2.goodFeaturesToTrack(gray,200,quality,20)
    if corners is not None:
        corners=np.int0(corners)
        
        for corner in corners:
            x,y = corner.ravel()
            cv2.circle(frame,(x,y), 3,(0,0,255),-1)

#op = np.hstack((img, thimg))
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) and ord('q') == 27:
        break

cap.release()
cv2.destroyAllWindows()
