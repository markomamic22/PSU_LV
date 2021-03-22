import matplotlib.pyplot as plt
import numpy as np
import skimage.io
import os
os.chdir("LV2")
img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()