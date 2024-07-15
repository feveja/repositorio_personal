#Dada una lista de temperaturas en grados Celsius, convertirlas a grados Fahrenheit utilizando NumPy.
import numpy as np

# Lista de temperaturas en grados Celsius
celsius_temperatures = [0, 10, 20, 30, 40]

# Convertir a arreglo de NumPy
celsius_arr = np.array(celsius_temperatures)

# Convertir Celsius a Fahrenheit: F = (C * 9/5) + 32
fahrenheit_arr = (celsius_arr * 9/5) + 32

# Imprimir los resultados
print("Temperaturas en Celsius:", celsius_arr)
print("Temperaturas en Fahrenheit:", fahrenheit_arr)
