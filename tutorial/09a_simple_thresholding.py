import numpy as np
import cv2

def show(title, img):
    cv2.imshow(title, img)
    cv2.imwrite("output/"+title+".jpg", img)

path = "../images/coins.png"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
show("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
show("Threshold Binary Inverse", threshInv)

coins = cv2.bitwise_and(image, image, mask = threshInv)
show("Coins", coins)
cv2.waitKey(0)

