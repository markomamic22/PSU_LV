import numpy as np
import matplotlib.pyplot as plt


xpoints = np.array([1.0,2.0,3.0,3.0,1.0])
ypoints = np.array([1.0,2.0,2.0,1.0,1.0])
plt.axis([0.0,4.0,0.0,4.0])
plt.plot(xpoints,ypoints)
plt.title('Primjer')
plt.xlabel('x os')
plt.ylabel('y os')
plt.show()