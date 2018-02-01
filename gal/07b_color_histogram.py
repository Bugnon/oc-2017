from matplotlib import pyplot as plt
import numpy as np
import cv2

path = "../images/beach.png"
image = cv2.imread(path)
cv2.imshow("Original", image)

chans = cv2.split(image)
colors = ("b", "g", "r")

plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

plt.savefig("output/histogram2.jpg")
plt.show()