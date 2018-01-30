The 6th chapter is the image processing chapter, here's the base image that we will be using during the whole explaination.

![06_Original](../output/06_Original.jpg)

# Translation
Translate the image from the given x, y values

`translate(img, 100, -50)`

![06_Translation](../output/06_Translation.jpg)


# Rotation
Rotate the image around the given point from the given value.

`rotate(img, 150, 50, 30)`

![06_Rotation](../output/06_Rotation.jpg)


# Resize
Resize the given image, if height isn't given or it is negative, it will keep the same ratio.

`resize(img, 150, 100)`

![06_Resize](../output/06_Resize.jpg)


# Flipping
Flip the image in the given direction, possible values are :
        - v for vertical
        - h for horizontal
        - b for both

`flip(img, "v")`

![06_Flipping](../output/06_Flipping.jpg)


# Crop
Crop the given image, from the start point to the end point.

`crop(img, 100, 50, 250, 150)`

![06_Crop](../output/06_Crop.jpg)


# Spliting
Split the image into the diffrent color channel.
Ex :

![06_Red](../output/06_Red.jpg)


![06_Green](../output/06_Green.jpg)


![06_Blue](../output/06_Blue.jpg)

