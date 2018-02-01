##Author: Gabriel Fleischer
##Organisation: Gymnase du Bugnon
##Date: 29.01.18

import numpy as np
import cv2

f = open("./md/08_blur_and_smooth.md", "w")
image = cv2.imread("./images/Visages.jpg")

def md(txt):
    f.write(txt + '\n')

def show(title, image):
    """Show and save the image, and create the .md line for it."""
    cv2.imshow(title, image)
    title = "08_" + title
    imagepath = "output/"+title+".jpg"
    cv2.imwrite(imagepath, image)
    md("\n![" + title + "](../" + imagepath + ")\n")
    
def gen_md_for(title, func, func_to_exec):
    md("## " + title)
    md(func.__doc__ + "\n")
    md("`" + func_to_exec + "`")
    md("")

#Averaging
def blur_avrg(image, radius):
	"""Blur the given image with the given size with the average blur methode."""
	return cv2.blur(image, (radius, radius))
	
#Gaussian
def blur_gaus(image, radius):
	"""Blur the given image with the given size with the gaussian blur methode."""
	return cv2.GaussianBlur(image, (radius, radius), 0)
	
#Median
def blur_med(image, radius):
	"""Blur the given image with the given size with the median blur methode."""
	return cv2.medianBlur(image, radius)
	
#Bilateral
def blur_bi(image, radius, color):
	"""Blur the given image with the given size with the blur_bi methode. Slower than the other methods"""
	return cv2.bilateralFilter(image, radius, color, color)
	
md("# Blur and Smooth")

show("Original", image)

gen_md_for("Average Methode", blur_avrg, "blur_avrg(image, 3)\nblur_avrg(image, 5)\nblur_avrg(image, 7)")
show("Average", np.hstack([
	blur_avrg(image, 3),
	blur_avrg(image, 5),
	blur_avrg(image, 7)]))
	
gen_md_for("Gaussian Methode", blur_gaus, "blur_gaus(image, 3)\nblur_gaus(image, 5)\nblur_gaus(image, 7)")
show("Gaussian", np.hstack([
	blur_gaus(image, 3),
	blur_gaus(image, 5),
	blur_gaus(image, 7)]))
	
gen_md_for("Median Methode", blur_med, "blur_med(image, 3)\nblur_med(image, 5)\nblur_med(image, 7)")
show("Median", np.hstack([
	blur_med(image, 3),
	blur_med(image, 5),
	blur_med(image, 7)]))
	
gen_md_for("Bilateral Methode", blur_bi, "blur_bi(image, 3, 15)\nblur_bi(image, 5, 30)\nblur_bi(image, 7, 50)")
show("Bilateral", np.hstack([
	blur_bi(image, 3, 15),
	blur_bi(image, 5, 30),
	blur_bi(image, 7, 50)]))
	
f.close()
cv2.waitKey(0)
