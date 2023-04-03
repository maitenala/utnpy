archivo = open ("c:/users/maite/documents/UTNPy/datos.txt")

import numpy as np

lista= []

for linea in archivo:
    lista.append(linea.split())

matriz = np.array(lista, dtype=float)

print(matriz)

archivo.close() 