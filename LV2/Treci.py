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