# Problema del cambio de monedas utilizando vuelta atrás (backtracking)

def coin_change_backtracking(coins, amount):
    # Backtracking
    # coins: lista de monedas
    # amount: cantidad a cambiar
    def backtrack(index, remaining_amount): # index: indice de la moneda actual
        if remaining_amount == 0: # Si la cantidad actual es 0
            return 0 # Retorna 0
        if remaining_amount < 0 or index == len(coins): # Si la cantidad actual es negativa o se ha alcanzado el final de la lista de monedas
            return float('inf') # Retorna infinito
        
        # No tomar la moneda actual
        not_take = backtrack(index + 1, remaining_amount)
        
        # Tomar la moneda actual
        take = float('inf')
        if coins[index] <= remaining_amount: # Si la moneda actual es menor o igual que la cantidad restante
            take = 1 + backtrack(index, remaining_amount - coins[index]) # Tomar la moneda actual
        
        return min(not_take, take)# Retorna el minimo entre no tomar la moneda actual y tomar la moneda actual
    
    result = backtrack(0, amount) # Llamada a la funcion de vuelta atrás
    return result if result != float('inf') else -1 # Retorna el minimo entre no tomar la moneda actual y tomar la moneda actual

# Pruebas
coins = [1, 2, 5]
amount = 11

print(coin_change_backtracking(coins, amount))  # Salida: 3

coins = [2]
amount = 3

print(coin_change_backtracking(coins, amount))  # Salida: -1

coins = [1]
amount = 0

print(coin_change_backtracking(coins, amount))  # Salida: 0
