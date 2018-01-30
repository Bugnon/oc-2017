import numpy as np
import cv2
import imutils

def show(title):
    cv2.imshow(title, flipped)
    cv2.imwrite("output/"+title+".jpg", flipped)
    
path = "../images/trex.png"
image = cv2.imread(path)
cv2.imshow("Original", image)

flipped = cv2.flip(image, 1)
show("Flipped Horizontally")

flipped = cv2.flip(image, 0)
show("Flipped Vertically")

flipped = cv2.flip(image, -1)
show("Flipped Horizontally & Vertically")

cv2.waitKey(0)
