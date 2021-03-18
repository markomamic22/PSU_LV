import numpy as np

a = np.array([6,2,9])
print (a.shape) 

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, num=30)
plt.plot(x, np.sin(x), '--', linewidth=1)
plt.plot(x, np.cos(x+np.pi/3), 'r-', linewidth=2)
plt.xlabel('x')
plt.ylabel('vrijednosti funkcije')
plt.title('sin i cos funkcija')
plt.show()