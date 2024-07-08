# Problema de la mochila 0/1 utilizando programación dinámica

def knapsack_dynamic_programming(weights, values, capacity):
    n = len(values)
    # Crear una tabla para almacenar los valores máximos
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]
    
    # Llenar la tabla de abajo hacia arriba
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Pruebas
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print(knapsack_dynamic_programming(weights, values, capacity))  # Salida: 220

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6

print(knapsack_dynamic_programming(weights, values, capacity))  # Salida: 65

weights = [5, 4, 6, 3]
values = [10, 40, 30, 50]
capacity = 10

print(knapsack_dynamic_programming(weights, values, capacity))  # Salida: 90
