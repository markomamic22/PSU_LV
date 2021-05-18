import keras
import os
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np

os.chdir('LV7')
filename = 'Screenshot_7.png'

img = mpimg.imread(filename)
img = color.rgb2gray(img)
img = resize(img, (28, 28))


plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')


# TODO: ucitaj model
model = keras.models.load_model('model')

# TODO: napravi predikciju 
res = model.predict(img)

# TODO: ispis rezultat
print("------------------------")
print(np.argmax(res))



