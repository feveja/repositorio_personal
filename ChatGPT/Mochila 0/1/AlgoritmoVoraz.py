# Problema de la mochila 0/1 utilizando un enfoque voraz (no garantiza la solución óptima)

def knapsack_greedy(weights, values, capacity):
    index = list(range(len(values)))
    # Calcular el valor por peso
    ratio = [v / w for v, w in zip(values, weights)]
    # Ordenar por valor por peso
    index.sort(key=lambda i: ratio[i], reverse=True)
    
    max_value = 0
    for i in index:
        if weights[i] <= capacity:
            capacity -= weights[i]
            max_value += values[i]
    
    return max_value

# Pruebas
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print(knapsack_greedy(weights, values, capacity))  # Salida: 160 (no óptimo)

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6

print(knapsack_greedy(weights, values, capacity))  # Salida: 65 (óptimo en este caso)

weights = [5, 4, 6, 3]
values = [10, 40, 30, 50]
capacity = 10

print(knapsack_greedy(weights, values, capacity))  # Salida: 90 (óptimo en este caso)
