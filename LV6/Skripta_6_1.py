import matplotlib as mpl
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
import joblib
import pickle
from sklearn.metrics._plot.confusion_matrix import plot_confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix


X, y = fetch_openml('mnist_784', return_X_y=True, as_frame=False, cache=True)


# TODO: prikazi nekoliko ulaznih slika
plt.imshow(X[0].reshape(28,28), cmap="gray")
plt.show()



# skaliraj podatke, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]


# TODO: izgradite vlastitu mrezu pomocu sckitlearn MPLClassifier 
mlp = MLPClassifier(verbose=True)
mlp.fit(X_train,y_train)

# TODO: evaluirajte izgradenu mrezu
print("Train set score: ", mlp.score(X_train,y_train))
print("Test set score: ", mlp.score(X_test,y_test))


matrix = confusion_matrix(mlp.predict(X_test),y_test)
print(matrix)
sns.heatmap(matrix, annot=True)
plt.show()

# spremi mrezu na disk
filename = "NN_model.sav"
joblib.dump(mlp, filename)

