import cv2
import numpy as np
#from deskew import deskew
global G_Mean, G_Median


class ImgLightCol:

    def __init__(self):
        pass

    def lightControl(self, image, f):
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        G_Mean = np.mean(np.array(image))
        G_Median = np.median(np.array(image))
        #print(mean, median)
        Contrast_Img = np.array(255*(image/255)**f, dtype='uint8')
        G_Mean = np.mean(np.array(Contrast_Img))
        G_Median = np.median(np.array(Contrast_Img))
        #print(mean, median)
        while G_Mean < 85 and G_Median < 85:
            f = f-0.2
            Contrast_Img = np.array(255*(image/255)**f, dtype='uint8')
            G_Mean = np.mean(np.array(Contrast_Img))
            G_Median = np.median(np.array(Contrast_Img))
            #print(G_Mean, G_Median)
        while G_Mean > 110 and G_Median > 110:
            f = f+0.2
            Contrast_Img = np.array(255*(image/255)**f, dtype='uint8')
            G_Mean = np.mean(np.array(Contrast_Img))
            G_Median = np.median(np.array(Contrast_Img))
            #print(G_Mean, G_Median)

        print("light conditioning done")
        return Contrast_Img
