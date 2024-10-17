import numpy as np

# Paso 1: Matriz de uso (Q = consultas, A = atributos)
# Supongamos que tenemos una relación con 4 atributos y 4 consultas como ejemplo.
matriz_uso = np.array([
    [1, 1, 1, 1],  # q1: usa A1, A2, A3, A4
    [0, 1, 1, 1],  # q2: usa A2, A3, A4
    [0, 1, 0, 1],  # q3: usa A2, A4
    [0, 0, 1, 1],  # q4: usa A3, A4
])

# Paso 2: Matriz de afinidad
def calcular_afinidad(matriz_uso, frecuencias):
    n_atributos = matriz_uso.shape[1]
    matriz_afinidad = np.zeros((n_atributos, n_atributos))
    
    # Calculamos la afinidad
    for i in range(n_atributos):
        for j in range(i, n_atributos):
            afinidad = 0
            for k, frecuencia in enumerate(frecuencias):
                if matriz_uso[k][i] == 1 and matriz_uso[k][j] == 1:
                    afinidad += frecuencia
            matriz_afinidad[i][j] = matriz_afinidad[j][i] = afinidad
    return matriz_afinidad

# Frecuencias de acceso por consulta
frecuencias = [15, 10, 25, 30]

# Generamos la matriz de afinidad
matriz_afinidad = calcular_afinidad(matriz_uso, frecuencias)
print("Matriz de Afinidad:")
print(matriz_afinidad)

# Paso 3: Algoritmo BEA (ordenación para maximizar afinidad)
def bond_energy_algorithm(matriz_afinidad):
    n_atributos = matriz_afinidad.shape[0]
    orden = [0]  # Inicialmente seleccionamos el primer atributo
    for i in range(1, n_atributos):
        mejor_posicion = 0
        mejor_contribucion = -np.inf
        # Intentamos colocar el siguiente atributo en cada posible posición
        for j in range(len(orden) + 1):
            contribucion = 0
            # Calculamos la contribución en la posición j
            if j > 0:
                contribucion += 2 * matriz_afinidad[orden[j-1], i]
            if j < len(orden):
                contribucion += 2 * matriz_afinidad[i, orden[j]]
            if j > 0 and j < len(orden):
                contribucion -= 2 * matriz_afinidad[orden[j-1], orden[j]]
            if contribucion > mejor_contribucion:
                mejor_contribucion = contribucion
                mejor_posicion = j
        # Insertamos el atributo en la mejor posición
        orden.insert(mejor_posicion, i)
    return orden

# Obtenemos el orden óptimo
orden_optimo = bond_energy_algorithm(matriz_afinidad)
print("Orden óptimo de atributos:")
print(orden_optimo)

# Paso 4: Fragmentación (dividimos los atributos en fragmentos basados en el orden)
def fragmentar(orden, n_fragmentos=2):
    fragmentos = []
    fragment_size = len(orden) // n_fragmentos
    for i in range(n_fragmentos):
        inicio = i * fragment_size
        if i == n_fragmentos - 1:
            fragmentos.append(orden[inicio:])  # El último fragmento contiene el resto
        else:
            fragmentos.append(orden[inicio:inicio + fragment_size])
    return fragmentos

# Fragmentamos los atributos
fragmentos = fragmentar(orden_optimo)
print("Fragmentos:")
for i, fragmento in enumerate(fragmentos):
    print(f"Fragmento {i+1}: Atributos {fragmento}")
