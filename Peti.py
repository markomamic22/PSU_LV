import numpy as np
import skimage as sk
from itertools import chain

def function(pikseli,broj_visina,broj_sirina):
    crna = np.zeros(((broj_sirina/2),(broj_visina/2)), dtype=int)
    bijela = 255*np.ones(((broj_sirina/2),(broj_visina/2)), dtype=int)

    

    