## Import the OpenCV library
import cv2

## Path to the image
path = "../images/trex.png"
 
## Read the image into memory and display it
image = cv2.imread(path)
cv2.imshow("Original", image)

## Read the pixel in the top left corner
(b, g, r) = image[200, 200]
print("Pixel at (200, 200) - Red={}, Green={}, Blue={}".format(r, g, b))

## Change the pixel in the top left corner
image[5, 5] = (0, 0, 255)
(b, g, r) = image[200, 200]
print("Pixel at (200, 200) - Red={}, Green={}, Blue={}".format(r, g, b))
cv2.imshow("Original", image)
image
cv2.imshow("changed", image)

## Extract a sub-image and display it
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

## Change a subregion and display it
image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)

## Wait for a key press
cv2.waitKey(0)