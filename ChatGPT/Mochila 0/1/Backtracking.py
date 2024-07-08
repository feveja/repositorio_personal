# Problema de la mochila 0/1 utilizando vuelta atrás (backtracking)

def knapsack_backtracking(weights, values, capacity):
    def backtrack(i, remaining_capacity):
        if i == len(weights) or remaining_capacity == 0:
            return 0
        if weights[i] > remaining_capacity:
            return backtrack(i + 1, remaining_capacity)
        return max(values[i] + backtrack(i + 1, remaining_capacity - weights[i]), backtrack(i + 1, remaining_capacity))

    return backtrack(0, capacity)

# Pruebas
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print(knapsack_backtracking(weights, values, capacity))  # Salida: 220

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6

print(knapsack_backtracking(weights, values, capacity))  # Salida: 65

weights = [5, 4, 6, 3]
values = [10, 40, 30, 50]
capacity = 10

print(knapsack_backtracking(weights, values, capacity))  # Salida: 90
