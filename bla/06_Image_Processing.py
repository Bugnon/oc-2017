import numpy as np
import imutils
import cv2

f = open('MD/06_image_processing.md', 'w')

def md(txt):
    f.write(txt+'\n')

md("# 6: Image processing")

def show(title, img):
##    cv2.imshow(title, img)
    img_path = "output/"+title+".jpg"
    cv2.imwrite(img_path, img)
    f.write(""+title+"\n\n")
    f.write("![image]("+'../'+img_path+")\n\n")

path = "images/3_visages.jpg"
image = cv2.imread(path)

show('06_Original', image)

## ============================================================
md("""
## Translation
A translation 2x3 floating point matrix `M` is used with the function
`cv2.warpAffine(img, M, (w, h))`.
```python
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
```
""")

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show("06_Shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show("06_Shifted Up and Left", shifted)

shifted = imutils.translate(image, 0, 100)
show("06_Shifted Down", shifted)
cv2.waitKey(0)

def translate(image,x,y):
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    
    return shifted
## ============================================================
(h, w) = image.shape[:2]
center = (w//2, h//2) #you want to rotate around the middle of the image

md("""
## Rotation
To rotate an image we need a 2x3 rotation matrix.
```python
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
```
""")
def rotate(image,angle,center = None, scale = 1.0):
    (h,w)=image.shape[2]
    
    if center is None:
        center = (w//2,h//2)
        
    M= cv2.getRotationMatrix2D(center,angle,scale)
    rotated =cv2.warpAffine(image,M,(w,h))
    
    return rotated

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
show("06_Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
show("06_Rotated by -90 Degrees", rotated)

rotated = imutils.rotate(image, 180)
show("06_Rotated by 180 Degrees", rotated)


## ============================================================
md("## Reseizing")
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0]*r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
show("06_Resized by Width", resized)

r = 50.0 / image.shape[0]             # height
dim = (int(image.shape[1] * r), 50)   # (width, hight)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
show("06_Resized by Height", resized)

resized = imutils.resize(image, width = 100)
show("06_Resized via Function", resized)

def resize(image,width = None,height = None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
        
    else:
        r= width / float(w)
        dim = width, int(h*r)
        
    resized = cv2.resize (image,dim,interpolation = inter)
    
    return resized

## ============================================================

md("""
## Flipping
Flipping an image can be done with the function `cv2.flip(img, dir)`.
""")

flipped = cv2.flip(image, 1)
show("06_Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
show("06_Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
show("06_Flipped Horizontally & Vertically", flipped)

## ============================================================
md("""
## Cropping
Extracting an image region (cropping) can be achieved by using
the NumPy array slicing.
```
cropped = image[30:120, 240:335]
```
""")

cropped = image[30:70, 200:250]
show("06_face_of_the_man", cropped)

## ============================================================
md("""
## Arithmetic
Testing basic arithmetic functions
""")
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
show("06_2_Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
show("06_2_Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
show("06_2_AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
show("06_2_OR", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
show("06_2_XOR", bitwiseXor)

bitwiseNot = cv2.bitwise_not(rectangle)
show("06_2_NOT_rectangle", bitwiseNot)

bitwiseNot = cv2.bitwise_not(circle)
show("06_2_NOT_circle", bitwiseNot)

## ============================================================
md("""
## Masking
Using a mask to take only the most important part of the picture.
""")

path = "../images/beach.png"
image = cv2.imread(path)
cv2.imshow("06_2_Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
(cx, cy) = (image.shape[1]//2, image.shape[0]//2)
d=75
cv2.rectangle(mask, (cx-d, cy-d), (cx+d, cy+d), 255, -1)
cv2.imshow("06_2_Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
show("06_2_Square Mask applied to image", masked)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cx, cy), 100, 255, -1)
cv2.imshow("06_2_Mask circle", mask)
masked = cv2.bitwise_and(image, image, mask=mask)
show("06_2_Circular Mask applied to image", masked)

## ============================================================
md("""
## Splitting And Merging Channels

__Splitting the channels__
""")

path = "images/lego_bricks_01.jpg"
image = cv2.imread(path)
cv2.imshow("06_3_Original", image)

(B, G, R) = cv2.split(image)

cv2.imshow("06_3_Red", R)
show("06_3_Red", R)
cv2.waitKey(0)
cv2.imshow("06_3_Green", G)
show("06_3_Green", G)
cv2.waitKey(0)
cv2.imshow("06_3_Blue", B)
show("06_3_Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("06_3_Merged", merged)
cv2.waitKey(0)

zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
show("06_3_red", cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
show("06_3_green", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
show("06_3_blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)



f.close()