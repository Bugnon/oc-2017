import numpy as np
import cv2
import imutils

def show(title, img):
    cv2.imshow(title, img)
    cv2.imwrite("output/"+title+".jpg", img)
    
path = "images/lego336*336.jpg"
image = cv2.imread(path)
cv2.imshow("Original", image)

cropped = image[40:220, 100:300]
show("orange lego", cropped)
cv2.waitKey(0)