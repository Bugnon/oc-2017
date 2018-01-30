import numpy as np
import cv2

def show(title, img):
    cv2.imshow(title, img)
    cv2.imwrite("output/"+title+".jpg", img)
    
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
show("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
show("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
show("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
show("OR", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
show("XOR", bitwiseXor)

bitwiseNot = cv2.bitwise_not(circle)
show("NOT", bitwiseNot)
cv2.waitKey(0)

