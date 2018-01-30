# Smoothing

## Averaging
Performing averaging blurring with
a 3 × 3 kernel *left*, 5 × 5 kernel *middle*,
and 7 × 7 kernel *right*
```python
blurred = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))])
```   

Averaged

![image](output/Averaged.jpg)


## Gaussian
Performing Gaussian blurring with a
3 × 3 kernel *left*, 5 × 5 kernel *middle*,
and 7 × 7 kernel *right*. Again,
our image becomes more blurred as
the kernel size increases, but is less
blurred than the average method
```python
blurred = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)])
```   

Gaussian

![image](output/Gaussian.jpg)


## Median
Applying the median blur method to
our image with increasing kernel
sizes of 3 *left*, 5 *middle*, and
7 *right*, respectively. Notice that
we are no longer creating a “motion
blur”.
```python
blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)])
```   

Median

![image](output/Median.jpg)


## Bilateral
Applying Bilateral blurring to our
image. As the diameter of the
neighborhood, color σ, and space σ
increases *from left to right*, our image
has noise removed, yet still retains
edges and does not appear to
be “motion blurred”.
```python
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)])
```   

Bilateral

![image](output/Bilateral.jpg)

