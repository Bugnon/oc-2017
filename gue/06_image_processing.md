# Image processing
Original

![image](output/Original.jpg)


## Translation
A translation 2x3 floating point matrix `M` is used with the function
`cv2.warpAffine(img, M, (w, h))`.
```python
M = np.float32([[1, 0, 50], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
```

Shifted_Down_and_Right

![image](output/Shifted_Down_and_Right.jpg)

Shifted_Up_and_Left

![image](output/Shifted_Up_and_Left.jpg)

Shifted_Down

![image](output/Shifted_Down.jpg)


## Rotation
To rotate an image we need a 2x3 rotation matrix.
```python
M = cv2.getRotationMatrix2D(center, 70, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
```

Rotated_by_70_Degrees

![image](output/Rotated_by_70_Degrees.jpg)

Rotated_by_-90_Degrees

![image](output/Rotated_by_-90_Degrees.jpg)

Rotated_by_180_Degrees

![image](output/Rotated_by_180_Degrees.jpg)

## Reseizing
Resized_by_Width

![image](output/Resized_by_Width.jpg)

Resized_by_Height

![image](output/Resized_by_Height.jpg)

Resized_via_Function

![image](output/Resized_via_Function.jpg)


## Flipping
Flipping an image can be done with the function `cv2.flip(img, dir)`.

Flipped_Horizontally

![image](output/Flipped_Horizontally.jpg)

Flipped_Vertically

![image](output/Flipped_Vertically.jpg)

Flipped_Horizontally_&_Vertically

![image](output/Flipped_Horizontally_&_Vertically.jpg)


## Cropping
Extracting an image region (cropping) can be achieved by using
the NumPy array slicing.
```
cropped = image[40:220, 100:300]```

orange_lego

![image](output/orange_lego.jpg)

