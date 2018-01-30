##Author: Gabriel Fleischer
##Organisation: Gymnase du Bugnon
##Date: 29.01.18

import numpy as np
import cv2

f = open("./md/06_image_processing.md", "w")
image = cv2.imread("./images/LEGO.jpg")

def md(txt):
    f.write(txt + '\n')

def show(title, image):
    """Show and save the image, and create the .md line for it."""
    cv2.imshow(title, image)
    title = "06_" + title
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

def translate(image, x, y):
    """Translate the image from the given x, y values"""
    #Creating the translation matrix
    M = np.float32([[1, 0, x], [0, 1, y]])
    m = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return m

def rotate(image, x, y, val):
    """Rotate the image around the given point from the given value."""
    (w, h) = image.shape[:2]
#   #Making sure the point is in the image
    if x < 0 or y < 0 or x > w or y > h:
        return
    center = (x, y)
    M = cv2.getRotationMatrix2D(center, val, 1.0)
    return cv2.warpAffine(image, M, (w, h))

def resize(image, w, h = -1):
    """Resize the given image, if height isn't given or it is negative, it will keep the same ratio."""
    if w < 1:
        return
    dim = (w, h)
    if h < 1:
        ratio = w/image.shape[1]
        dim = (w, int(image.shape[0]*ratio))
        
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
 
def flip(image, dir):
    """Flip the image in the given direction, possible values are :
        - v for vertical
        - h for horizontal
        - b for both"""
    val = 2
    if dir == "v":
        val = 0
    elif dir == "h":
        val = 1
    elif dir == "b":
        val = -1
    else:
        print("Unkown direction : " + dir)
    
    return cv2.flip(image, val)
    
def crop(image, x1, y1, x2, y2):
    """Crop the given image, from the start point to the end point."""
    cropped = image[y1:y2 , x1:x2]
    return cropped
    

def btiwise_and(image1, image2):
    """Apply the AND operation to the images."""
    return cv2.bitwise_and(image1, image2)    

def btiwise_or(image1, image2):
    """Apply the OR operation to the images."""
    return cv2.bitwise_or(image1, image2)

def btiwise_xor(image1, image2):
    """Apply the XOR operation to the images."""
    return cv2.bitwise_xor(image1, image2)

def btiwise_not(image):
    """Apply the NOT operation to the image."""
    return cv2.bitwise_not(image)    

def mask(image, mask):
    """Apply a mask to the given image."""
    return cv2.bitwise_and(image, image, mask = mask)

def split(image):
    """return the different color channels of the image. (R G B)"""
    zeros = np.zeros(image.shape[:2], dtype = "uint8")
    (B, G, R) = cv2.split(image)
    R = cv2.merge([zeros, zeros, R])
    G = cv2.merge([zeros, G, zeros])
    B = cv2.merge([B, zeros, zeros])
    return (R, G, B)

md("The 6th chapter is the image processing chapter, here's the base image that we will be using during the whole explaination.")

show("Original", image)

gen_md_for("Translation", translate, "translate(img, 100, -50)", image)
gen_md_for("Rotation", rotate, "rotate(img, 150, 50, 30)", image)
gen_md_for("Resize", resize, "resize(img, 150, 100)", image)
gen_md_for("Flipping", flip, "flip(img, \"v\")", image)
gen_md_for("Crop", crop, "crop(img, 100, 50, 250, 150)", image)

md("# Spliting")
md("Split the image into the diffrent color channel.")
md("Ex :")
(R, G, B) = split(image)
show("Red", R)
show("Green", G)
show("Blue", B)

f.close()
cv2.waitKey(0)