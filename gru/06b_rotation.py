import numpy as np
import cv2
import imutils

def show(title):
    cv2.imshow(title, rotated)
    cv2.imwrite("output/"+title+".jpg", rotated)
    
path = "../images/trex.png"
image = cv2.imread(path)

(h, w) = image.shape[:2]
center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
show("Rotated by 45 Degrees")

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
show("Rotated by -90 Degrees")

rotated = imutils.rotate(image, 180)
show("Rotated by 180 Degrees")

cv2.waitKey()