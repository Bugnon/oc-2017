import numpy as np
import cv2

def show(title):
    cv2.imshow(title, shifted)
    cv2.imwrite("output/"+title+".jpg", shifted)

path = "../images/trex.png"
image = cv2.imread(path)

cv2.imshow("Original", image)

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show("Shifted Down and Right")

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show("Shifted Up and Left")

shifted = imutils.translate(image, 0, 100)
show("Shifted Down")
cv2.waitKey(0)
