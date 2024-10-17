import numpy as np

# Paso 1: Generar la matriz de uso
def generar_matriz_uso():
    # Definimos manualmente la matriz de uso
    return np.array([
        [0, 1, 1, 0],  # q1
        [1, 1, 1, 0],  # q2
        [1, 0, 0, 1],  # q3
        [0, 0, 1, 0]   # q4
    ])

# Paso 2: Calcular la matriz de afinidad
def calcular_matriz_afinidad(matriz_uso, frecuencias):
    num_atributos = matriz_uso.shape[1]
    matriz_afinidad = np.zeros((num_atributos, num_atributos))
    
    for i in range(num_atributos):
        for j in range(num_atributos):
            for consulta in range(matriz_uso.shape[0]):
                if matriz_uso[consulta, i] == 1 and matriz_uso[consulta, j] == 1:
                    matriz_afinidad[i, j] += frecuencias[consulta]
    
    return matriz_afinidad

# Paso 3: Algoritmo BEA (Bond Energy Algorithm) para ordenar atributos
def bond_energy_algorithm(matriz_afinidad):
    n = matriz_afinidad.shape[0]
    orden = [0]  # Comienza con la primera columna fija
    columnas_disponibles = list(range(1, n))
    
    while columnas_disponibles:
        mejor_contribucion = -np.inf
        mejor_columna = None
        mejor_posicion = None
        
        for columna in columnas_disponibles:
            for pos in range(len(orden) + 1):
                contribucion = 0
                if pos > 0:
                    contribucion += np.sum(matriz_afinidad[orden[pos - 1], columna])
                if pos < len(orden):
                    contribucion += np.sum(matriz_afinidad[columna, orden[pos]])
                
                # Considerar también las afinidades con las columnas a ambos lados
                if pos > 0 and pos < len(orden):
                    contribucion += matriz_afinidad[orden[pos - 1], columna] + matriz_afinidad[columna, orden[pos]]
                
                if mejor_contribucion < contribucion:
                    mejor_contribucion = contribucion
                    mejor_columna = columna
                    mejor_posicion = pos
        
        # Insertar la mejor columna en el mejor lugar
        orden.insert(mejor_posicion, mejor_columna)
        columnas_disponibles.remove(mejor_columna)
    
    return orden
# Paso 4: Aplicar el algoritmo de agrupamiento para obtener la fragmentación
def obtener_fragmentos(matriz_afinidad, orden):
    matriz_ca = matriz_afinidad[np.ix_(orden, orden)]
    
    umbral_fragmentacion = np.median(matriz_ca)
    fragmentos = [[], []]
    
    for i, fila in enumerate(matriz_ca):
        if np.sum(fila) >= umbral_fragmentacion:
            fragmentos[0].append(orden[i])
        else:
            fragmentos[1].append(orden[i])
    
    return matriz_ca, fragmentos

# Ejecución del proceso
matriz_uso = generar_matriz_uso()

# Frecuencias de acceso para las consultas (ejemplo de frecuencias)
frecuencias = [25, 25, 45, 30]

# Matriz de afinidad
matriz_afinidad = calcular_matriz_afinidad(matriz_uso, frecuencias)
print("Matriz de Afinidad:")
print(matriz_afinidad)

# Obtener el mejor orden con BEA
orden = bond_energy_algorithm(matriz_afinidad)
print("Orden de los atributos (BEA):")
print(orden)

# Fragmentación final
matriz_ca, fragmentos = obtener_fragmentos(matriz_afinidad, orden)
print("Matriz CA ordenada:")
print(matriz_ca)
print("Mejor fragmentación (dos fragmentos):")
print(fragmentos)
