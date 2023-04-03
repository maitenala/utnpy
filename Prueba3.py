import numpy as np
import matplotlib.pyplot as plt

matriz= np.loadtxt("c:/users/maite/documents/UTNPy/datos.txt",dtype=float)

x = matriz[:, 0]
y = matriz[:, 1]
z = matriz[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.title('Datos en 3D')
plt.show()