import numpy as np

def bond_energy_algorithm(query_access_matrix, query_attribute_matrix):
    # Calcular la energía de enlace entre columnas
    bond_energy = np.dot(query_access_matrix.T, query_attribute_matrix)
    
    # Agrupar columnas según la energía de enlace
    fragments = []
    while bond_energy.size > 0:
        max_index = np.unravel_index(np.argmax(bond_energy), bond_energy.shape)
        fragments.append(max_index)
        bond_energy = np.delete(bond_energy, max_index[0], axis=0)
        bond_energy = np.delete(bond_energy, max_index[1], axis=1)

    return fragments

# Ejemplo de uso
query_access_matrix = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 1]])
query_attribute_matrix = np.array([[1, 0], [0, 1], [1, 1]])

fragments = bond_energy_algorithm(query_access_matrix, query_attribute_matrix)
print("Fragmentos resultantes:", fragments)