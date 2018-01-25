from matplotlib import pyplot as plt
import numpy as np
import cv2

def histogram_2d(title, img):
    chans = cv2.split(img)
    colors = "BGR"

    ## figsize in inches, results in (200x600 pixels)
    fig = plt.figure(figsize=(9,3))

    ## Plot a 2D color histogram for green and blue
    for i in range(3):
        sub = 131+i
        j = (i+1)%3
        ax = fig.add_subplot(sub)
        hist = cv2.calcHist([chans[i], chans[j]], [0, 1], None, [32, 32], [0, 256, 0, 256])
        p = ax.imshow(hist, interpolation = "nearest")
        ax.set_title(colors[i]+" and "+colors[j])
    plt_path = "output/"+title.replace(" ", "_")+".jpg"    
    plt.savefig(plt_path)        

path = "../images/beach.png"
image = cv2.imread(path)
cv2.imshow("Original", image)

histogram_2d("2D color histogram", image)
    
chans = cv2.split(image)
colors = ("b", "g", "r")

## figsize in inches, results in (200x600 pixels)
fig = plt.figure(figsize=(6,2))


## Plot a 2D color histogram for green and blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for G and B")
##plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for G and R")
##plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for B and R")
##plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0]))

plt.savefig("output/histogram2D.jpg")
plt.show()

