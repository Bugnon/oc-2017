import cv2

def resize(image,width = None,height = None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
        
    else:
        r= width / float(w)
        dim = width, int(h*r)
        
    resized = cv2.resize (image,dim,interpolation = inter)
    
    return resized
    
path="coin.jpg"
img=cv2.imread(path)
cropped = img[0:1000, 0:1250]
img2=resize(cropped,400)
cv2.imwrite('2'+path,img2)