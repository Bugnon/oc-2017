from matplotlib import pyplot as plt
import numpy as np
import cv2

f = open('07_histograms.md', 'w')

def md(txt):
    f.write(txt+'\n')

def show(title, img):
##    cv2.imshow(title, img)
    img_path = "output/"+title.replace(" ", "_")+".jpg"
    cv2.imwrite(img_path, img)
    f.write(""+title+"\n\n")
    f.write("![image]("+img_path+")\n\n")    

## ==========================================================
md("# Histograms")
md("## Grayscale histograms")

path = "../images/beach.png"
image = cv2.imread(path)

img = cv2.imshow("Original", image)
print(img)
show("Original image", image)
key = cv2.waitKey(500)
print(key)
 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
show("Image changed to gray-scale", image)

hist = cv2.calcHist([image.copy()], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

plt_path = "output/histogram.jpg"
plt.savefig(plt_path)
f.write("![image]("+plt_path+")\n\n")    

##plt.show()
key = cv2.waitKey(100)
print(key)


## ==========================================================
md("## Color histograms")

def histogram(title, img):
    chans = cv2.split(img)
    colors = ("b", "g", "r")

    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])
    
    plt_path = "output/"+title.replace(" ", "_")+".jpg"
    plt.savefig(plt_path)
    f.write(title+"\n\n")
    f.write("![image]("+plt_path+")\n\n")

path = "../images/beach.png"
img = cv2.imread(path)
histogram("RGB color histogram", img)
histogram("Grayscale histogram", image)

## ==========================================================
md("## 2D color histograms")

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
    f.write(title+"\n\n")
    f.write("![image]("+plt_path+")\n\n")
    
path = "../images/beach.png"
image = cv2.imread(path)    
histogram_2d("2D color histogram", image)

f.close()