import numpy as np
import os
from tensorflow import keras
import tensorflow as tf
import seaborn as sns
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.python.keras.backend import conv2d
from tensorflow.python.keras.utils.metrics_utils import ConfusionMatrix

os.chdir('LV7')

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
plt.imshow(x_train[0].reshape(28,28), cmap="gray")
plt.show()

# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu
model = Sequential([
    keras.Input(shape=input_shape),
    layers.Conv2D(32, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Conv2D(16, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Flatten(),
    layers.Dense(30, activation='relu'),
    layers.Dense(10, activation='softmax'),
])
model.summary()



# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
# podesavanje parametara procesa ucenja
model.compile(loss='categorical_crossentropy',
 optimizer='adam',
 metrics=['accuracy'])


# TODO: provedi ucenje mreze
model.fit(x_train_s, y_train_s, epochs=10, batch_size=32)


# TODO: Prikazi test accuracy i matricu zabune
loss_and_metrics = model.evaluate(x_test_s, y_test_s, batch_size=128)
print(loss_and_metrics)
#x=tf.math.confusion_matrix(labels=y_test, predictions=model.predict(x_test_s,batch_size=128))
#print("Confusion matrix\n", x)
# TODO: spremi model
model.save('model')

