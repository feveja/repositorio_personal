# Parece que olvidé importar numpy. Voy a corregir eso.
import numpy as np

# La matriz de afinidad observada en la imagen proporcionada
affinity_matrix_example = np.array([[85, 85, 85, 85],
                                    [85, 320, 190, 320],
                                    [85, 190, 215, 215],
                                    [85, 320, 215, 345]])

# Funciones necesarias para aplicar BEA nuevamente
def bond(Ax, Ay, affinity_matrix):
    """Calcula el valor bond entre las columnas Ax y Ay usando la matriz de afinidad"""
    return np.sum(affinity_matrix[:, Ax] * affinity_matrix[:, Ay])

def contribution(Ai, Ak, Aj, affinity_matrix):
    """Calcula la contribución para insertar la columna Ak entre Ai y Aj"""
    bond_ik = bond(Ai, Ak, affinity_matrix)
    bond_kj = bond(Ak, Aj, affinity_matrix)
    bond_ij = bond(Ai, Aj, affinity_matrix)
    return 2 * (bond_ik + bond_kj) - 2 * bond_ij

def bond_energy_algorithm(affinity_matrix):
    """Aplica el algoritmo BEA a la matriz de afinidad dada"""
    n = affinity_matrix.shape[1]
    columns_positioned = [0]  # Empezamos con la primera columna arbitraria (puede ser cualquier columna)
    unpositioned_columns = list(range(1, n))  # Las columnas que aún no están en la matriz agrupada
    
    # Inicializamos la matriz agrupada con la primera columna
    while unpositioned_columns:
        best_column = None
        best_position = None
        best_contribution = -np.inf
        
        # Iteramos sobre todas las columnas no posicionadas
        for k in unpositioned_columns:
            # Intentamos insertar la columna en cada posición posible (al inicio, al final, o entre dos columnas)
            for pos in range(len(columns_positioned) + 1):
                if pos == 0:
                    # Colocamos al inicio
                    Ai = columns_positioned[0]
                    contribution_value = contribution(k, Ai, Ai, affinity_matrix)
                elif pos == len(columns_positioned):
                    # Colocamos al final
                    Aj = columns_positioned[-1]
                    contribution_value = contribution(Aj, k, Aj, affinity_matrix)
                else:
                    # Colocamos entre Ai y Aj
                    Ai = columns_positioned[pos - 1]
                    Aj = columns_positioned[pos]
                    contribution_value = contribution(Ai, k, Aj, affinity_matrix)
                
                # Si la contribución es mejor que la anterior, actualizamos el mejor valor
                if contribution_value > best_contribution:
                    best_column = k
                    best_position = pos
                    best_contribution = contribution_value
        
        # Insertamos la mejor columna encontrada en la mejor posición
        columns_positioned.insert(best_position, best_column)
        unpositioned_columns.remove(best_column)
    
    # Reordenamos las filas en base al nuevo orden de las columnas
    clustered_affinity_matrix = affinity_matrix[:, columns_positioned][columns_positioned, :]
    
    return clustered_affinity_matrix, columns_positioned

# Aplicar el BEA con el ejemplo que proporcionaste en la imagen
clustered_matrix_example, order_example = bond_energy_algorithm(affinity_matrix_example)
print(clustered_matrix_example, order_example)

def calculate_group_accesses(affinity_matrix, diagonal_point):
    """
    Calcula los valores de CTQ, CBQ y COQ según el punto de la diagonal elegido.
    
    Args:
    affinity_matrix: Matriz de afinidad.
    diagonal_point: El punto de la diagonal que divide TA y BA (índice del punto de corte).
    
    Returns:
    CTQ, CBQ, COQ: Números de acceso para los diferentes grupos.
    """
    # División de la matriz en dos partes según el punto de corte diagonal
    TA = affinity_matrix[:diagonal_point, :diagonal_point]
    BA = affinity_matrix[diagonal_point:, diagonal_point:]
    OQ = affinity_matrix[:diagonal_point, diagonal_point:]
    
    # Cálculo de accesos
    CTQ = np.sum(TA)  # Accesos de TA
    CBQ = np.sum(BA)  # Accesos de BA
    COQ = np.sum(OQ)  # Accesos cruzados entre TA y BA
    
    return CTQ, CBQ, COQ

def maximize_access(affinity_matrix):
    """
    Encuentra el punto de la diagonal que maximiza la función CTQ * CBQ - COQ^2.
    
    Args:
    affinity_matrix: Matriz de afinidad.
    
    Returns:
    best_point: El mejor punto en la diagonal.
    max_value: El valor máximo de la función objetivo.
    """
    n = affinity_matrix.shape[0]
    best_point = None
    max_value = -np.inf
    
    # Iterar sobre todos los puntos posibles en la diagonal
    for diagonal_point in range(1, n):
        CTQ, CBQ, COQ = calculate_group_accesses(affinity_matrix, diagonal_point)
        
        # Evaluar la función objetivo
        value = CTQ * CBQ - COQ**2
        
        # Verificar si es el mejor valor hasta ahora
        if value > max_value:
            max_value = value
            best_point = diagonal_point
    
    return best_point, max_value

# Aplicar el algoritmo a la matriz de ejemplo (que ya fue reorganizada)
best_diagonal_point, max_value = maximize_access(clustered_matrix_example)

print(best_diagonal_point, max_value)
