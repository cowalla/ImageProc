import numpy as np
from PIL import Image
img = Image.open("use.jpg")
img = img.convert('1')
# x, y = img.size[0], img.size[1]
# total_length = x*y
# pixelMap = img.load()
# data = img.getdata()
# from copy import deepcopy
# from binary_filter import on_off
# from binary_filter import rgb

# 
# img.putdata(outData[::-1])
img.save("changed.jpg", "JPEG")