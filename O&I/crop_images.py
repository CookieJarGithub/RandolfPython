#%%

from numpy import *
from matplotlib.pyplot import *
from imageio import imread
from PIL import Image

f = open("gt.txt", "r")
lines_original = f.readlines()
lines = []

IMG_DIRECTORY = "img/"
CROPPED_IMG_DIRECTORY = "cropped/"
IMG_FORMAT = ".png"

# Parses each line into a set of integer values. Transfers them to new "lines" list
for line in lines_original:
    current_line = line.split(",")
    for index, value in enumerate(current_line):
        current_line[index] = int(value)
    lines.append(current_line)

# Takes each value from every line[] in lines[] and crops each image accordingly.
for index, line in enumerate(lines):
    img_id = line[0]
    img_str = IMG_DIRECTORY + "{:06d}".format(img_id) + IMG_FORMAT
    lettuce_id, x, y, w, h = line[1], line[2], line[3], line[4], line[5]

    im = imread(img_str)
    im_cropped_array = im[y:y+h, x:x+h]
    im_cropped = Image.fromarray(im_cropped_array)
    im_cropped.save(CROPPED_IMG_DIRECTORY + str("{:06d}".format(img_id)) + "-" + str(lettuce_id) + IMG_FORMAT)

f.close()
# %%
