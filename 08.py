#8.Write a NumPy program to create a 2d array with 1 on the border and 0 inside
#Ejemplo= Escribe un programa en Numpy para crear una matriz 2d con unos en el borde y ceros en el medio.

import numpy as np
x = np.ones((5,5))
print("Matriz Original: ")
print(x)
print("Bordes de uno y ceros en el medio...")
x[1:-1,1:-1]=0
print(x)
