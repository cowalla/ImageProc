import numpy as np
from PIL import Image
img = Image.open("use.jpg")
x, y = img.size[0], img.size[1]
total_length = x*y
pixelMap = img.load()
data = img.getdata()
from copy import deepcopy
from binary_filter import on_off
from binary_filter import rgb

#data is an array of sets, each one representing a pixel value. the array is flattened

outData = []
for i in range(0, total_length):
	dat = data[i]
	if (i < y or i > x * (y - 1)):
		outData.append(dat)
	if i > y and i < x * (y - 1):
		# outData.append(rgb(dat, 155))
		outData.append(rgb(dat, 100))

img.putdata(outData[::-1])
img.save("changed.jpg", "JPEG")



