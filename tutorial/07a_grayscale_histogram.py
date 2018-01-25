from matplotlib import pyplot as plt
import numpy as np
import cv2

f = open('07_histograms.md', 'w')

def md(txt):
    f.write(txt+'\n')

md("# Image processing")

def show(title, img):
    cv2.imshow(title, img)
    cv2.imwrite("output/"+title+".jpg", img)

path = "../images/beach.png"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

f.close()

hist = cv2.calcHist([image.copy()], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

plt.savefig("output/histogram.jpg")
plt.show()
cv2.waitKey(0)