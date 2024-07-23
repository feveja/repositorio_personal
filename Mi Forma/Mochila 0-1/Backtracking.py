def knapsack_01_backtracking(values, weights, capacity):
    def backtrack(index, current_weight, current_value):
        nonlocal max_value
        if current_weight > capacity:
            return
        if index == len(values):
            max_value = max(max_value, current_value)
            return
        
        # Caso en el que no se toma el objeto
        backtrack(index + 1, current_weight, current_value)
        
        # Caso en el que se toma el objeto
        backtrack(index + 1, current_weight + weights[index], current_value + values[index])
    
    max_value = 0
    backtrack(0, 0, 0)
    return max_value

# Ejemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack_01_backtracking(values, weights, capacity))  # Salida esperada: 220