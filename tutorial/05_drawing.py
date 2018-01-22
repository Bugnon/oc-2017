import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")    
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

def update():
    """Show the image in the "Canvas" window and wait for key."""
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)


cv2.line(canvas, (0, 0), (300, 300), green)
update()

cv2.line(canvas, (300, 0), (0, 300), red, 3)
update()

cv2.rectangle(canvas, (10, 10), (60, 60), green)
update()

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
update()

cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
update()

cv2.imwrite("output/05a_drawing.jpg", canvas)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(cx, cy) = (canvas.shape[1]//2, canvas.shape[0]//2)

for r in range(0, 175, 25):
    cv2.circle(canvas, (cx, cy), r, white)
update()
cv2.imwrite("output/05b_circles.jpg", canvas)

canvas = np.zeros((300, 300, 3), dtype="uint8")  
for i in range(0, 25):
    radius = np.random.randint(5, high=100)
    color = np.random.randint(0, high=256, size = (3,)).tolist()
    pt = np.random.randint(0, high=300, size = (2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)
update()
cv2.imwrite("output/05c_disks.jpg", canvas)

    