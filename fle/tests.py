## Import the OpenCV library
import cv2

## Path to the image
path = "../images/trex.png"
 
## Read the image into memory
image = cv2.imread(path)

## Print some image parameters to the console
w = image.shape[1]
h = image.shape[0]
