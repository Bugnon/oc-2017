import numpy as np
import cv2

def show(title, img):
    cv2.imshow(title, img)
    cv2.imwrite("output/"+title+".jpg", img)

path = "../images/coins.png"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)

edged = cv2.Canny(image, 30, 150)
show("Edges", edged)

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image".format(len(cnts)))

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    
    print("Coin #{}".format(i+1))
    coin = image[y:y+h, x:x+w]
    cv2.imshow("Coin", coin)
    
    mask = np.zeros(image.shape[:2], dtype = "uint8")
    ((cx, cy), r) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(cx), int(cy)), int(r), 255, -1)
    
    mask = mask[y:y+h, x:x+w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))

cv2.waitKey(0)
