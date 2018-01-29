import cv2

path = "../images/trex.png"
image = cv2.imread(path)
img = cv2.imshow("Original", image)
print(img)
key = cv2.waitKey(1000)
print(key)
 