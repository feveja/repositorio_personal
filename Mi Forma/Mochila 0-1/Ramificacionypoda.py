# Problema de la mochila 0/1 utilizando Ramificación y Poda en Python

def branch_and_bound_knapsack(values, weights, capacity):
    n = len(values)
    indices = list(range(n))
    
    # Función para calcular la cota superior
    def upper_bound(curr_weight, curr_value, k):
        upper_bound_value = curr_value
        upper_bound_weight = curr_weight
        
        while k < n and upper_bound_weight + weights[indices[k]] <= capacity:
            upper_bound_weight += weights[indices[k]]
            upper_bound_value += values[indices[k]]
            k += 1
        
        if k < n:
            upper_bound_value += (capacity - upper_bound_weight) * values[indices[k]] / weights[indices[k]]
        
        return upper_bound_value
    
    # Función para calcular la cota inferior
    def lower_bound(curr_weight, curr_value, k):
        lower_bound_value = curr_value
        lower_bound_weight = curr_weight
        
        for i in range(k, n):
            if lower_bound_weight + weights[indices[i]] <= capacity:
                lower_bound_weight += weights[indices[i]]
                lower_bound_value += values[indices[i]]
            else:
                remaining_capacity = capacity - lower_bound_weight
                lower_bound_value += values[indices[i]] * (remaining_capacity / weights[indices[i]])
                break
        
        return lower_bound_value
    
    def knapsack_recursive(curr_weight, curr_value, k):
        nonlocal max_value
        nonlocal best_set
        if curr_weight <= capacity and curr_value > max_value:
            max_value = curr_value
            best_set = set(indices[:k])
        
        if k == n:
            return
        
        if upper_bound(curr_weight, curr_value, k) <= max_value:
            return
        
        if lower_bound(curr_weight, curr_value, k) > max_value:
            knapsack_recursive(curr_weight + weights[indices[k]], curr_value + values[indices[k]], k + 1)
        
        knapsack_recursive(curr_weight, curr_value, k + 1)
    
    max_value = 0
    best_set = set()
    knapsack_recursive(0, 0, 0)
    
    return max_value, best_set

# Ejemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, best_set = branch_and_bound_knapsack(values, weights, capacity)
print(f"El beneficio máximo es: {max_value}")
print(f"Conjunto de objetos seleccionados: {best_set}")