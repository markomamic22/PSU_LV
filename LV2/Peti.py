import numpy as np
import matplotlib.pyplot as plt

def funkcija(pikseli,broj_visina,broj_sirina):
    crna = np.zeros((pikseli,pikseli))
    bijela = 255*np.ones((pikseli,pikseli))


    img = [[]]
    for i in range(int(broj_visina/2)):
        img= np.vstack((crna,bijela))
    
    plt.figure(1)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.show()

funkcija(5,10,10)



"""import numpy as np
import matplotlib.pyplot as plt
check = np.zeros((5, 5))
check[::2, 1::2] = 1
check[1::2, ::2] = 1
plt.matshow(check, cmap='gray')
plt.show()"""