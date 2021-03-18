import numpy as np
import matplotlib.pyplot as plt
import os


os.chdir("LV2")
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
plt.scatter(data[:,0],data[:,3],c='b',s=data[:,2])
plt.show()