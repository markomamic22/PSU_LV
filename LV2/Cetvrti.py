from re import X
import matplotlib.pyplot as plt
import numpy as np
import skimage.io
import os

from skimage.util.dtype import img_as_bool
os.chdir("LV2")
img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()

a = 100*np.ones(img.shape)
img = np.add(img,a)
row, col = img.shape
for i in range(row):
    for j in range(col):
        if(img[i][j] >= 255):
            img[i][j] = 255
        if(img[i][j]  <0):
            img[i][j] = 0


plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
img2 = np.zeros((col,row))
for j in range(row):
    img2[:,row-1-j] = img[j,:]

plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.show()

for j in range(row):
    img2[:,j] = img[j,:]
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.show()