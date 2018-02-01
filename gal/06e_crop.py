import numpy as np
import cv2
import imutils

def show(title, img):
    cv2.imshow(title, img)
    cv2.imwrite("output/"+title+".jpg", img)
    
path = "../images/trex.png"
image = cv2.imread(path)
cv2.imshow("Original", image)

cropped = image[30:120, 240:335]
show("T-Rex Face", cropped)
cv2.waitKey(0)