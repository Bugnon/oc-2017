import numpy as np
import cv2

def show(title, img):
    cv2.imshow(title, img)
    cv2.imwrite("output/"+title+".jpg", img)

path = "../images/beach.png"
image = cv2.imread(path)
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
(cx, cy) = (image.shape[1]//2, image.shape[0]//2)
d=75
cv2.rectangle(mask, (cx-d, cy-d), (cx+d, cy+d), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
show("Square Mask applied to image", masked)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cx, cy), 100, 255, -1)
cv2.imshow("Mask circle", mask)
masked = cv2.bitwise_and(image, image, mask=mask)
show("Circular Mask applied to image", masked)

cv2.waitKey(0)