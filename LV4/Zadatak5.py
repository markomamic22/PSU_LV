#ulazne veličine- koliko ih je sto oznacava koji, mse za svaki model - koji tip modela s kojim veličinama, koje sam odabrao te prikaz modela - za izvještaj
import pandas
import seaborn as sb
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error



boston = load_boston()
data = boston.data
df =  pandas.DataFrame.from_dict(data)
ticklabels = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
values = boston.target
df[13] = values[:]
corr_matrix = df.corr()
mask = np.zeros_like(corr_matrix)
mask[np.triu_indices_from(mask)] = True
fig, ax = plt.subplots(figsize=(10,8))
with sb.axes_style("white"):
    sb.heatmap(corr_matrix, mask=mask, square=True, xticklabels=ticklabels, yticklabels=ticklabels, cmap="coolwarm", annot=True,linewidths=0.5, ax=ax)
plt.show()

#dropanje podataka koji ne utječu na vrijednosti ili su multikorelatnosti
df.columns = ticklabels
df = df.drop(['ZN','CHAS',"MEDV","RAD","TAX","DIS","AGE"],1)
print(df)

#plotanje podatka kako bi vidjeli bi vidjeli linearnu ovisnost
plt.figure(figsize=(20, 15))
features = ['CRIM','INDUS','NOX','RM','PTRATIO','B','LSTAT']
target = values
for i, col in enumerate(features):
    plt.subplot(3, int(len(features)/2) , i+1)
    x = df[col]
    y = target
    plt.scatter(x, y, marker='o')
    plt.xlabel(col)
    plt.ylabel('MEDV')
plt.show()

#prije i poslije regularizacije lstat
plt.scatter(df['LSTAT'],target)
plt.xlabel('LSTAT')
plt.ylabel('MEDV')
plt.show()
df['LSTAT'] = df['LSTAT'].apply(np.log)
plt.scatter(df['LSTAT'],target)
plt.xlabel('Normalized LSTAT')
plt.ylabel('MEDV')
plt.show()
#pravljenje test i train setova
X_train, X_test, y_train, y_test = train_test_split(df,y,test_size=0.2)

linear = LinearRegression()
linear.fit(X_train,y_train)
y_pred = linear.predict(X_test)

#provjera performansi
r2 = linear.score(X_test, y_test)
rmse = (np.sqrt(mean_squared_error(y_test, y_pred)))
print("The model performance is")
print("--------------------------------------")
print('R2 score is {}'.format(r2))
print('RMSE is {}'.format(rmse))
print("\n")

plt.scatter(y_test, y_pred)
plt.xlabel('Prava vrijednost')
plt.ylabel('Predviđena vrijednost')
plt.show()