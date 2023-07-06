#%%

from numpy import *
from matplotlib.pyplot import *
from imageio import imread
import os

IMG_DIR = "img/"

subfolder = random.choice(os.listdir(IMG_DIR)) + "/"
image_file = random.choice(os.listdir(IMG_DIR + subfolder))
im = imread(IMG_DIR + subfolder + image_file)

imshow(im)
# %%
