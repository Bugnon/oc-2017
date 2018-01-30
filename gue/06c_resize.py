import numpy as np
import cv2
import imutils

def show(title):
    cv2.imshow(title, resized)
    cv2.imwrite("output/"+title+".jpg", resized)
    
path = "../images/trex.png"
image = cv2.imread(path)
cv2.imshow("Original", image)

r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0]*r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
show("Resized (Width)")

r = 50.0 / image.shape[0]             # height
dim = (int(image.shape[1] * r), 50)   # (width, hight)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
show("Resized (Height)")

resized = imutils.resize(image, width = 100)
show("Resized via Function")

cv2.waitKey(0)
