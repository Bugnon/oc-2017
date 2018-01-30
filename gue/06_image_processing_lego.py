#28.01.18
#Bugnon 3MOCINFO
#Author Albert Guedj
#Inspired from Raphael Holzer's 06a_translation.py

import numpy as np
import imutils
import cv2

f = open('06_image_processing.md', 'w')

def md(txt):
    f.write(txt+'\n')

md("# Image processing")

def show(title, img):
##    cv2.imshow(title, img)
    img_path = "output/"+title+".jpg"
    cv2.imwrite(img_path, img)
    f.write(""+title+"\n\n")
    f.write("![image]("+img_path+")\n\n")

path = "images/lego336*336.jpg"
image = cv2.imread(path)

show('Original', image)

## ============================================================
md("""
## Translation
A translation 2x3 floating point matrix `M` is used with the function
`cv2.warpAffine(img, M, (w, h))`.
```python
M = np.float32([[1, 0, 50], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
```
""")

M = np.float32([[1, 0, 50], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show("Shifted_Down_and_Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show("Shifted_Up_and_Left", shifted)

shifted = imutils.translate(image, 0, 130)
show("Shifted_Down", shifted)
cv2.waitKey(0)

## ============================================================
(h, w) = image.shape[:2]
center = (w//2, h//2)

md("""
## Rotation
To rotate an image we need a 2x3 rotation matrix.
```python
M = cv2.getRotationMatrix2D(center, 70, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
```
""")

M = cv2.getRotationMatrix2D(center, 70, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
show("Rotated_by_70_Degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
show("Rotated_by_-90_Degrees", rotated)

rotated = imutils.rotate(image, 180)
show("Rotated_by_180_Degrees", rotated)


## ============================================================
md("## Reseizing")
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0]*r))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
show("Resized_by_Width", resized)

r = 50.0 / image.shape[0]             # height
dim = (int(image.shape[1] * r), 50)   # (width, hight)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
show("Resized_by_Height", resized)

resized = imutils.resize(image, width = 100)
show("Resized_via_Function", resized)


md("""
## Flipping
Flipping an image can be done with the function `cv2.flip(img, dir)`.
""")

flipped = cv2.flip(image, 1)
show("Flipped_Horizontally", flipped)

flipped = cv2.flip(image, 0)
show("Flipped_Vertically", flipped)

flipped = cv2.flip(image, -1)
show("Flipped_Horizontally_&_Vertically", flipped)

## ============================================================
md("""
## Cropping
Extracting an image region (cropping) can be achieved by using
the NumPy array slicing.
```
cropped = image[40:220, 100:300]```
""")

cropped = image[40:220, 100:300]
show("orange_lego", cropped)
cv2.waitKey(0)
f.close()