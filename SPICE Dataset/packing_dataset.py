#%%

import torch
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np

resize_normalize = transforms.Compose([
            transforms.Resize((96,96)),
            transforms.ToTensor(),
        ])

SPICE = torchvision.datasets.ImageFolder('img',transform=resize_normalize)

random_img = np.random.randint(0, len(SPICE) - 1)

labels = ['maybe usable', 'not usable', 'usable']
plt.title(labels[SPICE[random_img][1]])
plt.imshow(SPICE[random_img][0].permute(1,2,0))
# %%
