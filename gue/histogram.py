#28.01.18
#Bugnon 3MOCINFO
#Author Albert Guedj
#Inspired from various Raphael Holzer's .py files

from matplotlib import pyplot as plt
import numpy as np
import imutils
import cv2

f = open('07_histogram_lego.md', 'w')

def md(txt):
    f.write(txt+'\n')


md("# Histogram")

def show(title, img):
    cv2.imshow(title, img)
    img_path = "output/"+title+".jpg"
    cv2.imwrite(img_path, img)
    f.write(""+title+"\n\n")
    f.write("![image]("+img_path+")\n\n")

path = "images/lego336*336.jpg"
image = cv2.imread(path)

show('Original', image)

## ============================================================

md("""
## Grayscale histograms
Computing a grayscale histogram of the image
""")
  
hist= cv2.calcHist([image.copy()], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.savefig("output/grayscale_histogram.jpg")
path = "output/grayscale_histogram.jpg"
gray = cv2.imread(path)
resized = imutils.resize(gray, width = 400)
show("grayscale_histogram",resized)

## ============================================================

md("""
## Color histograms
for each Red, Green, and Blue channel of the image
""")


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

plt.savefig("output/histogram_color.jpg")
path = "output/histogram_color.jpg"
color = cv2.imread(path)
resized = imutils.resize(color, width = 400)
show("histogram_color",resized)

## ============================================================

md("""
## Computing 2D
color histograms for each combination of Red, Green, and Blue channels
""")

fig = plt.figure()

# Plot a 2D color histogram for green and blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D for B and R")
plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0]))

plt.savefig("output/histogram_2D.jpg")
path = "output/histogram_2D.jpg"
hist2d = cv2.imread(path)
resized = imutils.resize(hist2d, width = 400)
show("histogram_2D",resized)

## ============================================================
md("""
## Equalization
*Left*: The original image.
*Right*: The image after applying histogram
equalizationcolor histograms for each combination of Red, Green, and Blue channels
""")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

img = np.hstack([image, eq])
##cv2.imshow("Histogram Equalization", img)
cv2.imwrite("output/equalizeHist.jpg", img)
path = "output/equalizeHist.jpg"
hist_eq = cv2.imread(path)
resized = imutils.resize(hist_eq, width = 400)
show("equalizeHist",resized)

## ============================================================
md("""
## Equalization
*Up*: Color histograms for the red, green,
and blue channels .
*Down*: Color histograms for the masked image
""")

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
    
    plt.savefig("output/"+title+".jpg")
        
path = "images/lego336*336.jpg"
image = cv2.imread(path)
plot_histogram(image, "Histogram_for_Original_Image")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", masked)
plot_histogram(image, "Histogram_for_Masked_Image", mask = mask)

path = "output/Histogram_for_Original_Image.jpg"
hist_original = cv2.imread(path)
resized = imutils.resize(hist_original, width = 400)
show("Histogram_for_Original_Image",resized)

path = "output/Histogram_for_Masked_Image.jpg"
hist_mask = cv2.imread(path)
resized = imutils.resize(hist_mask, width = 400)
show("Histogram_for_Masked_Image",resized)





f.close()