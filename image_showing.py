#%%

from numpy import *
from matplotlib.pyplot import *
from imageio import imread

im = imread("miku.jpg")

WIDTH = im.shape[1]
HEIGHT = im.shape[0]
WIDTH_HALF = WIDTH // 2
HEIGHT_HALF = HEIGHT // 2

print(im[0][0][0])
"""
Image representation in numpy is handled via *3D* arrays
This can be verified by the print above, which returns a value
One can also inspect the shape of the image array via im.shape
"""

# The image format is [y, x] for some reason
im_topleft = im[0 : HEIGHT_HALF, 0 : WIDTH_HALF]
im_topright = im[0 : HEIGHT_HALF, WIDTH_HALF : WIDTH]
im_bottomleft = im[HEIGHT_HALF : HEIGHT, 0 : WIDTH_HALF]
im_bottomright = im[HEIGHT_HALF : HEIGHT, WIDTH_HALF : WIDTH]
imshow(im_topleft)
# %%
