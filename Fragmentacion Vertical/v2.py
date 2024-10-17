import numpy as np

# Paso 1: Matriz de uso - ingresada por el usuario
matriz_uso = np.array([
    [1, 1, 1, 1],  # Ejemplo para Q1
    [0, 1, 1, 1],  # Ejemplo para Q2
    [0, 1, 0, 1],  # Ejemplo para Q3
    [0, 0, 1, 1]   # Ejemplo para Q4
])

# Paso 2: Frecuencias de acceso - ingresada por el usuario
frecuencias_acceso = np.array([
    [15, 20, 10],  # Q1 en sitios S1, S2, S3
    [15, 10, 25],  # Q2 en sitios S1, S2, S3
    [30, 20, 10],  # Q3 en sitios S1, S2, S3
    [3, 6, 5]      # Q4 en sitios S1, S2, S3
])

# Paso 3: Calcular la matriz de afinidad usando frecuencias de acceso
def calcular_matriz_afinidad(matriz_uso, frecuencias_acceso):
    num_atributos = matriz_uso.shape[1]
    matriz_afinidad = np.zeros((num_atributos, num_atributos))

    for i in range(num_atributos):
        for j in range(i, num_atributos):
            afinidad = 0
            for q, uso_q in enumerate(matriz_uso):
                if uso_q[i] == 1 and uso_q[j] == 1:
                    afinidad += np.sum(frecuencias_acceso[q])  # Ajuste de cálculo afinidad
            matriz_afinidad[i, j] = afinidad
            matriz_afinidad[j, i] = afinidad  # Asegurar simetría
    
    return matriz_afinidad

matriz_afinidad = calcular_matriz_afinidad(matriz_uso, frecuencias_acceso)
print("Matriz de Afinidad:\n", matriz_afinidad)

# Paso 4: Aplicar BEA con evaluación de todas las posiciones posibles
def BEA(matriz_afinidad):
    num_atributos = matriz_afinidad.shape[0]
    orden = [0]  # Empezar con el primer atributo fijo
    for k in range(1, num_atributos):
        mejor_orden = None
        mejor_contribucion = -np.inf
        for i in range(len(orden) + 1):
            nuevo_orden = orden[:i] + [k] + orden[i:]
            contribucion = calcular_contribucion(matriz_afinidad, nuevo_orden)
            if contribucion > mejor_contribucion:
                mejor_contribucion = contribucion
                mejor_orden = nuevo_orden
        orden = mejor_orden
    return matriz_afinidad[np.ix_(orden, orden)], orden

def calcular_contribucion(matriz, orden):
    contribucion = 0
    for i in range(1, len(orden) - 1):
        contribucion += matriz[orden[i - 1], orden[i]] + matriz[orden[i], orden[i + 1]]
    return contribucion

matriz_CA, orden_CA = BEA(matriz_afinidad)
print("Matriz CA ordenada:\n", matriz_CA)

# Paso 5: Algoritmo de Agrupamiento con variables CTQ, CBQ, y COQ más detalladas
def algoritmo_agrupamiento(matriz_CA):
    mejor_puntaje = -np.inf
    mejor_division = None

    for i in range(1, matriz_CA.shape[0]):
        TA = matriz_CA[:i, :i]
        BA = matriz_CA[i:, i:]
        OQ = matriz_CA[:i, i:]

        CTQ = np.sum(TA)
        CBQ = np.sum(BA)
        COQ = np.sum(OQ)

        puntaje = CTQ * CBQ - COQ ** 2
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_division = i

    return mejor_division, mejor_puntaje

division, puntaje = algoritmo_agrupamiento(matriz_CA)
print(f"Mejor división en la posición {division} con puntaje {puntaje}")
