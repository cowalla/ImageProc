import numpy as np
from PIL import Image
img = Image.open("use.jpg")
x, y = img.size[0], img.size[1]
total_length = x*y
pixelMap = img.load()
data = img.getdata()
from copy import deepcopy
#data is an array of sets, each one representing a pixel value. the array is flattened

outData = []
for i in range(0, total_length):
	# if i % y != 0 and i % y != ( y - 1 ):
	# 	# i is not on a horizontal boundary (important when performing NN calcs)
		if i > x and i < (x - 1) * ( y ):
	# 		# i is not on a vertical boundary
			outData.append(data[i])
			
img.putdata(outData)
img.save("changed.jpg", "JPEG")
