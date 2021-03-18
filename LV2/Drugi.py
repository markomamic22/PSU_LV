import numpy as np
import matplotlib.pyplot as plt


i=0
v = []
counter = [0,0,0,0,0,0]
for i in range(100):

    x= np.random.randint(1,7)
    v.append(x)
    if(v[i]==1):
        counter[0] += 1
    elif(v[i]==2):
        counter[1] += 1
    elif(v[i]==3):
        counter[2] += 1 
    elif(v[i]==4):
        counter[3] += 1 
    elif(v[i]==5):
        counter[4] += 1 
    elif(v[i]==6):
        counter[5] += 1     
        

plt.hist(v, bins=6)
plt.show()    

