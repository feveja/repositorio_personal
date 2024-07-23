import numpy as np
#Ejercicio 1: Suma de Vectores
#Enunciado: Escribe una función que tome dos vectores como entrada y devuelva su suma.
def suma_vectores(vec1, vec2):
    return np.add(vec1, vec2)

# Ejemplo de uso
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
resultado = suma_vectores(vector1, vector2)
print("La suma de los vectores es:", resultado)

#Ejercicio 2: Producto Escalar
#Enunciado: Escribe una función que calcule el producto escalar entre dos vectores.
def producto_escalar(vec1, vec2):
    return np.dot(vec1, vec2)

# Ejemplo de uso
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
resultado = producto_escalar(vector1, vector2)
print("El producto escalar de los vectores es:", resultado)

#Ejercicio 3: Generación de Matriz Aleatoria
#Enunciado: Escribe una función que genere una matriz de tamaño especificado, con números aleatorios entre 0 y 1.
def matriz_aleatoria(filas, columnas):
    return np.random.rand(filas, columnas)

# Ejemplo de uso
filas = 3
columnas = 3
matriz = matriz_aleatoria(filas, columnas)
print("Matriz aleatoria:")
print(matriz)