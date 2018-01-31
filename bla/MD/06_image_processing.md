# 6: Image processing
06_Original

![image](../output/06_Original.jpg)


## Translation
A translation 2x3 floating point matrix `M` is used with the function
`cv2.warpAffine(img, M, (w, h))`.
```python
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
```

06_Shifted Down and Right

![image](../output/06_Shifted Down and Right.jpg)

06_Shifted Up and Left

![image](../output/06_Shifted Up and Left.jpg)

06_Shifted Down

![image](../output/06_Shifted Down.jpg)


## Rotation
To rotate an image we need a 2x3 rotation matrix.
```python
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
```

06_Rotated by 45 Degrees

![image](../output/06_Rotated by 45 Degrees.jpg)

06_Rotated by -90 Degrees

![image](../output/06_Rotated by -90 Degrees.jpg)

06_Rotated by 180 Degrees

![image](../output/06_Rotated by 180 Degrees.jpg)

## Reseizing
06_Resized by Width

![image](../output/06_Resized by Width.jpg)

06_Resized by Height

![image](../output/06_Resized by Height.jpg)

06_Resized via Function

![image](../output/06_Resized via Function.jpg)


## Flipping
Flipping an image can be done with the function `cv2.flip(img, dir)`.

06_Flipped Horizontally

![image](../output/06_Flipped Horizontally.jpg)

06_Flipped Vertically

![image](../output/06_Flipped Vertically.jpg)

06_Flipped Horizontally & Vertically

![image](../output/06_Flipped Horizontally & Vertically.jpg)


## Cropping
Extracting an image region (cropping) can be achieved by using
the NumPy array slicing.
```
cropped = image[30:120, 240:335]
```

06_face_of_the_man

![image](../output/06_face_of_the_man.jpg)


## Arithmetic
Testing basic arithmetic functions

06_2_Rectangle

![image](../output/06_2_Rectangle.jpg)

06_2_Circle

![image](../output/06_2_Circle.jpg)

06_2_AND

![image](../output/06_2_AND.jpg)

06_2_OR

![image](../output/06_2_OR.jpg)

06_2_XOR

![image](../output/06_2_XOR.jpg)

06_2_NOT_rectangle

![image](../output/06_2_NOT_rectangle.jpg)

06_2_NOT_circle

![image](../output/06_2_NOT_circle.jpg)


## Masking
Using a mask to take only the most important part of the picture.

06_2_Square Mask applied to image

![image](../output/06_2_Square Mask applied to image.jpg)

06_2_Circular Mask applied to image

![image](../output/06_2_Circular Mask applied to image.jpg)


## Splitting And Merging Channels

__Splitting the channels__

06_3_Red

![image](../output/06_3_Red.jpg)

06_3_Green

![image](../output/06_3_Green.jpg)

06_3_Blue

![image](../output/06_3_Blue.jpg)

06_3_red

![image](../output/06_3_red.jpg)

06_3_green

![image](../output/06_3_green.jpg)

06_3_blue

![image](../output/06_3_blue.jpg)

