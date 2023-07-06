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

plt.imshow(SPICE[0][0].permute(1,2,0))
# %%
