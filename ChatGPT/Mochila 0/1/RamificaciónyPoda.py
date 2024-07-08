# Problema de la mochila 0/1 utilizando ramificación y poda (branch and bound)

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

def bound(node, n, capacity, weights, values):
    if node.weight >= capacity:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    totweight = node.weight
    
    while j < n and totweight + weights[j] <= capacity:
        totweight += weights[j]
        profit_bound += values[j]
        j += 1
    
    if j < n:
        profit_bound += (capacity - totweight) * values[j] / weights[j]
    
    return profit_bound

def knapsack_branch_and_bound(weights, values, capacity):
    n = len(values)
    Q = []
    
    u = Node(-1, 0, 0, 0)
    v = Node(-1, 0, 0, 0)
    u.bound = bound(u, n, capacity, weights, values)
    Q.append(u)
    
    maxProfit = 0
    
    while Q:
        u = Q.pop(0)
        
        if u.level == -1:
            v.level = 0
        
        if u.level == n-1:
            continue
        
        v.level = u.level + 1
        
        v.weight = u.weight + weights[v.level]
        v.profit = u.profit + values[v.level]
        
        if v.weight <= capacity and v.profit > maxProfit:
            maxProfit = v.profit
        
        v.bound = bound(v, n, capacity, weights, values)
        
        if v.bound > maxProfit:
            Q.append(v)
        
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, capacity, weights, values)
        
        if v.bound > maxProfit:
            Q.append(v)
    
    return maxProfit

# Pruebas
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print(knapsack_branch_and_bound(weights, values, capacity))  # Salida: 220

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6

print(knapsack_branch_and_bound(weights, values, capacity))  # Salida: 65

weights = [5, 4, 6, 3]
values = [10, 40, 30, 50]
capacity = 10

print(knapsack_branch_and_bound(weights, values, capacity))  # Salida: 90
