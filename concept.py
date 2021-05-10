import numpy as np
from PIL import Image

file = "images/original/1.png"

img = Image.open(file)
rgb_im = img.convert("RGB")
arr = np.array(rgb_im)

print(arr.shape)

print(arr[0:540].shape)  # first row

#img.show()
