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

path = "../images/trex.png"
image = cv2.imread(path)

show('Original', image)

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
show("Shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show("Shifted Up and Left", shifted)

shifted = imutils.translate(image, 0, 100)
show("Shifted Down", shifted)
cv2.waitKey(0)

## ============================================================
(h, w) = image.shape[:2]
center = (w//2, h//2)

md("""
## Rotation
To rotate an image we need a 2x3 rotation matrix.
```python
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
```
""")

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
show("Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
show("Rotated by -90 Degrees", rotated)

rotated = imutils.rotate(image, 180)
show("Rotated by 180 Degrees", rotated)


## ============================================================
md("## Reseizing")
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0]*r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
show("Resized by Width", resized)

r = 50.0 / image.shape[0]             # height
dim = (int(image.shape[1] * r), 50)   # (width, hight)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
show("Resized by Height", resized)

resized = imutils.resize(image, width = 100)
show("Resized via Function", resized)


md("""
## Flipping
Flipping an image can be done with the function `cv2.flip(img, dir)`.
""")

flipped = cv2.flip(image, 1)
show("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
show("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
show("Flipped Horizontally & Vertically", flipped)

## ============================================================
md("""
## Cropping
Extracting an image region (cropping) can be achieved by using
the NumPy array slicing.
```
cropped = image[30:120, 240:335]
```
""")

cv2.rect(

cropped = image[30:120, 240:335]
show("T-Rex Face", cropped)
cv2.waitKey(0)
f.close()