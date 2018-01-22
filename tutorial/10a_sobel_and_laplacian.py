import numpy as np
import cv2

def show(title, img):
    cv2.imshow(title, img)
    cv2.imwrite("output/"+title+".jpg", img)

path = "../images/coins.png"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
show("Laplacian", lap)

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

show("Sobel X", sobelX)
show("Sobel Y", sobelY)
show("Sobel Combined", sobelCombined)

cv2.waitKey(0)
