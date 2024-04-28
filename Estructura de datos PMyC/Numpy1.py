import numpy as np
#Los mas usados
#np.array(): Convierte una lista o tupla de Python en un arreglo NumPy.
arr = np.array([1, 2, 3, 4, 5])
#np.zeros(): Crea un arreglo de ceros.
zeros_arr = np.zeros((3, 3))  # Crea un arreglo 3x3 de ceros
#np.ones(): Crea un arreglo de unos.
ones_arr = np.ones((2, 2))  # Crea un arreglo 2x2 de unos

#No tan usados  
#np.arange(): Crea un arreglo con valores espaciados uniformemente dentro de un rango.
range_arr = np.arange(1, 10, 2)  # Crea un arreglo con valores de 1 a 9 con paso de 2
#np.linspace(): Crea un arreglo con valores espaciados uniformemente entre dos números.
linspace_arr = np.linspace(0, 1, 5)  # Crea un arreglo con 5 valores entre 0 y 1

#Operaciones matematicas con Numpy
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

sum_arr = arr1 + arr2  # Suma de arreglos
mul_arr = arr1 * arr2  # Multiplicación de arreglos elemento por elemento
dot_product = np.dot(arr1, arr2)  # Producto punto

#Acceso a elementos
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[0, 0])  # Accede al elemento en la primera fila y primera columna
print(arr[1])     # Accede a la segunda fila completa
print(arr[:, 1])  # Accede a la segunda columna completa

#Otras Funciones de Numpy
#np.sum(), np.mean(), np.max(), np.min(): Calculan la suma, media, máximo y mínimo de los elementos de un arreglo, respectivamente.
#np.reshape(): Cambia la forma de un arreglo.
#np.transpose(): Transpone un arreglo.
#np.concatenate(), np.vstack(), np.hstack(): Concatenan arreglos.
#np.random.rand(), np.random.randn(): Generan arreglos de números aleatorios.