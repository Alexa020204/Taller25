# 9. Write a NumPy program to add a border (filled with 0's) around an existing array
# Español: Escribe un programa Numpy que agregue un borde(ceros) al rededor de una matrix existente.
import numpy as np
x =np.ones((3,3))
print("Matríz Original:")
print(x)
print("Cero en el borde y unos dentro de la matríz")
x = np.pad(x, pad_width=1, mode="constant", constant_values=0)
print(x)
