## Import the OpenCV library
import cv2

## Path to the image
path = "../images/trex.png"
 
## Read the image into memory and display it
image = cv2.imread(path)
cv2.imshow("Original", image)

## Read the pixel in the top left corner
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red={}, Green={}, Blue={}".format(r, g, b))

## Change the pixel in the top left corner
for i in range(256):
    for k in range(256):
        for x in range(256):
            image[0+i, 0+k] = (0+i, 0+k, 0+x)
            (b, g, r) = image[0, 0]
            print("Pixel at (0, 0) - Red={}, Green={}, Blue={}".format(r, g, b))
            
cv2.imshow("Original", image)

## Extract a sub-image and display it
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)


## Change a subregion and display it
image[0:100, 0:100] = (1, 8, 71)
cv2.imshow("Updated", image)

## Wait for a key press
cv2.waitKey(0)