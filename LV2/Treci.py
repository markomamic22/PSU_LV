import numpy as np
import matplotlib.pyplot as plt
import os


os.chdir("LV2")
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
plt.scatter(data[:,0],data[:,3],c='b',s=(data[:,5]*25))
plt.ylabel('hp')
plt.xlabel('mpg')
plt.show()

max_mpg = max(data[:,0])
min_mpg = min(data[:,0])
average_mpg = np.average(data[:,0])

print("Maksimalna vrijednost mpg je: ",max_mpg)
print("Minimalna vrijednost mpg je: ", min_mpg)
print("Srednja vrijednost mpg je: ", average_mpg)

i=0
indexes = []
for i in range(len(data[:,1])):
    if data[i,1]==6:
        indexes.append(i)

i=0
max_6 = 0
min_6 = max_mpg
sum_6 = 0

for i in range(len(indexes)):
    if data[indexes[i],0] > max_6:
        max_6 = data[indexes[i],0]
    elif data[indexes[i],0] <min_6:
        min_6 = data[indexes[i],0]
    sum_6 += data[indexes[i],0]

print("Max vrijednost 6 cilindra mpg je: ", max_6)
print("Min vrijednost 6 cilindra mpg je: ", min_6)
print("Srednja vrijednost 6 cilindra mpg je: ", (sum_6/len(indexes)))