import numpy as np
import matplotlib.pyplot as plt

matriz= np.loadtxt("c:/users/maite/documents/UTNPy/datos.txt",dtype=float)
print(matriz)

plt.plot(matriz)
plt.title('Datos')
plt.show()