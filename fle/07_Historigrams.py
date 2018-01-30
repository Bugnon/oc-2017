##Author: Gabriel Fleischer
##Organisation: Gymnase du Bugnon
##Date: 29.01.18
from matplotlib import pyplot as plt
import numpy as np
import cv2

f = open("./md/07_Histogram.md", "w")
image = cv2.imread("./images/Plaque.jpg")

def md(txt):
    f.write(txt + '\n')

def show(title, image):
    """Show and save the image, and create the .md line for it."""
    cv2.imshow(title, image)
    title = "07_" + title
    imagepath = "output/"+title+".jpg"
    cv2.imwrite(imagepath, image)
    md("\n![" + title + "](../" + imagepath + ")\n")
    
def gen_md_for(title, func, func_to_exec, img):
    md("# " + title)
    md(func.__doc__ + "\n")
    md("`" + func_to_exec + "`")
    exec("img2 = " + func_to_exec)
    exec("show(title, img2)")
    md("")
   
md("# Histograms")

md("The chapter 7 is about the histograms, here are some exemples of what we can do with the following image :")
   
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
show("Original", image)

hist = cv2.calcHist([gray.copy()], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

plt.savefig("output/histogram.jpg")
plt.show()

md("# Gray Histogram")

md("Here's the histogram of the image in gray :")
md("![Histogram](../output/histogram.jpg)")


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


md("# Color Histogram")

md("Here's the histogram of the image in color :")
md("![Color Histogram](../output/histogram2.jpg)")

fig = plt.figure()

## Plot a 2D color histogram for green and blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for G and B")
plt.colorbar(p)

## Green and Red
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for G and R")
plt.colorbar(p)
##Blue and Red
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for B and R")
plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0]))

plt.savefig("output/histogram2D.jpg")
plt.show()




md("# 2D Color Histogram")

md("This histogram shows the combination of colors in the picture.")
md("![2D Color Histogram](../output/histogram2D.jpg)")

eq = cv2.equalizeHist(gray)

img = np.hstack([gray, eq])

md("# Equalizer")

md("Equalizing an image is finding the perfect contrast to use the most pixels.")


show("Equalized", img)

def plot_histogram(image, title, mask = None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])
    
    plt.savefig("output/mask_histogram.jpg")
    
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (20,20), (200, 170), 255, -1)

md("# Histogram with mask")
md("We can use a mask for the histogram, with the following mask, here's the histogram we get :")

show("Mask", mask)

plot_histogram(image, "Histogram for Masked Image", mask = mask)

md("![Histogram_with_mask](../output/mask_histogram.jpg)")
f.close()