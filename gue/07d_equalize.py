import numpy as np
import cv2

path = "../images/beach.png"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

img = np.hstack([image, eq])
cv2.imshow("Histogram Equalization", img)
cv2.imwrite("output/equalizeHist.jpg", img)
cv2.waitKey(0)