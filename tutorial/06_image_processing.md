# Image processing
Original

![image](output/Original.jpg)


## Translation
A translation 2x3 floating point matrix `M` is used with the function
`cv2.warpAffine(img, M, (w, h))`.
```python
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
```

Shifted Down and Right

![image](output/Shifted%20Down%20and%20Right.jpg)

Shifted Up and Left

![image](output/Shifted%20Up%20and%20Left.jpg)

Shifted Down

![image](output/Shifted%20Down.jpg)


## Rotation
To rotate an image we need a 2x3 rotation matrix.
```python
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
```

Rotated by 45 Degrees

![image](output/Rotated%20by%2045%20Degrees.jpg)

Rotated by -90 Degrees

![image](output/Rotated%20by%20-90%20Degrees.jpg)

Rotated by 180 Degrees

![image](output/Rotated%20by%20180%20Degrees.jpg)

## Reseizing
Resized by Width

![image](output/Resized%20by%20Width.jpg)

Resized by Height

![image](output/Resized%20by%20Height.jpg)

Resized via Function

![image](output/Resized%20via%20Function.jpg)


## Flipping
Flipping an image can be done with the function `cv2.flip(img, dir)`.

Flipped Horizontally

![image](output/Flipped%20Horizontally.jpg)

Flipped Vertically

![image](output/Flipped%20Vertically.jpg)

Flipped Horizontally & Vertically

![image](output/Flipped Horizontally%20%26%20Vertically.jpg)


## Cropping
Extracting an image region (cropping) can be achieved by using
the NumPy array slicing.
```
cropped = image[30:120, 240:335]
```

T-Rex Face

![image](output/T-Rex%20Face.jpg)

