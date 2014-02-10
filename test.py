import numpy as np
from PIL import Image
img = Image.open("use.jpg")
x, y = img.size[0], img.size[1]
total_length = x*y
pixelMap = img.load()
data = img.getdata()
#data is an array of sets, each one representing a pixel value. the array is flattened

def on_off(value, eps):
	if value < eps:
		return 0
	else:
		return 100

	
#plan now is to:
# create a function that will set all pixels in data to on or off
# render that as an image file
# write it to an external file

# 
# in the i-dir, the +1 elt is i + 1. in the j-dir the +1 elt is j + x
ep = 30
for i in range(0, x * y):
	if i % x != 0 and i % x != ( x - 1 ):
		# i is not on a horizontal boundary (important when performing NN calcs)
		if i > x and i < x * ( y - 1 ):
			print i
			# i is not on a vertical boundary
			temp = data[i]
			data[i] = (on_off(temp[i][0], ep), on_off(temp[i][1], ep), on_off(temp[i][2], ep))

data
