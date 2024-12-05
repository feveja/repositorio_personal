import numpy as np

# (a) Generar la matriz M
A = np.array([[5, -1, 0, -1, 0, 1],
              [-1, 8, 0, 0, -2, 0],
              [0, 0, 1, 0, 0, 0],
              [-1, 0, 0, 4, -2, 0],
              [0, -2, 0, -2, 8, 0],
              [1, 0, 0, 0, 0, 7]])

B = np.zeros((6, 6))   # La matriz Theta (B) es de ceros
C = 2 * np.eye(6)      # C es una matriz identidad de 6x6 multiplicada por 2
D = np.eye(6)          # D es una matriz identidad de 6x6

# Construimos la matriz M
M = np.block([[A, B, D],
               [B, C, B],
               [D, B, C]])

# Imprimir la matriz M
print("La matriz M es:")
print(M)
def es_diagonal_dominante(matriz):
    filas = len(matriz)
    
    for i in range(filas):
        suma = 0
        for j in range(filas):
            if i != j:
                suma += abs(matriz[i][j])
        
        if abs(matriz[i][i]) <= suma:
            return False  # No es estrictamente dominante
    
    return True  # Es estrictamente dominante

# Ejemplo de uso
matriz = M
if es_diagonal_dominante(matriz):
    print("La matriz es estrictamente diagonal dominante.")
else:
    print("La matriz NO es estrictamente diagonal dominante.")
    

def es_diagonal_dominante2(matriz):
    # Convertimos la lista a un array de NumPy si no lo es ya
    matriz = np.array(matriz)
    
    # Obtenemos el número de filas
    filas = matriz.shape[0]
    
    for i in range(filas):
        # Suma de los valores absolutos de la fila, excluyendo el elemento diagonal
        suma = np.sum(np.abs(matriz[i])) - np.abs(matriz[i, i])
        
        # Verificamos la condición de dominancia estricta
        if np.abs(matriz[i, i]) <= suma:
            return False  # No es estrictamente dominante
    
    return True  # Es estrictamente dominante
# Ejemplo de uso
matriz = M
if es_diagonal_dominante(matriz):
    print("La matriz es estrictamente diagonal dominante.")
else:
    print("La matriz NO es estrictamente diagonal dominante.")