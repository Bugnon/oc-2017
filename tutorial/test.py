import cv2

path = "../images/trex.png"
image = cv2.imread(path)
cv2.imshow("Original", image)
cv2.waitKey(0)
