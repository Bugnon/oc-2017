## Import the OpenCV library
import cv2

## Path to the image
path = "../images/trex.png"
 
## Read the image into memory
image = cv2.imread(path)

## Print some image parameters to the console
print("width: ", image.shape[1])
print("height: ", image.shape[0])
print("channels: ", image.shape[2])

## Display the image on the screen
cv2.imshow("Image", image)

## Wait for a key press
cv2.waitKey(0)

## Write the file to a new file in the local directory
cv2.imwrite("output/03_newimage.jpg", image)
