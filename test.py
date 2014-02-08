import numpy as np
from PIL import Image
img = Image.open("use.jpg")
x, y = img.size[0], img.size[1]
pixelMap = img.load()
data = img.getdata()
#data is an array of sets, each one representing a pixel value. the array is flattened

def on_off(value, eps):
	if value < eps
		return 0
	else
		return 100
