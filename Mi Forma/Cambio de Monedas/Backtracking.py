def cambio_monedas_backtracking(monedas, cantidad): 
    # Funcion de vuelta atrás
    # Remain: Cantidad restante
    # Path: Lista de monedas tomadas
    # Index: Indice de la moneda actual
    def backtrack(remain, path, index): 
        if remain == 0: # Si la cantidad actual es 0
            soluciones.append(path) # Retorna la lista de monedas
            return # Retorna la lista de monedas    
        for i in range(index, len(monedas)): # Si la cantidad actual es negativa o se ha alcanzado el final de la lista de monedas
            if monedas[i] <= remain: # Si la moneda actual es menor o igual que la cantidad restante
                backtrack(remain - monedas[i], path + [monedas[i]], i) # Tomar la moneda actual
    
    monedas.sort(reverse=True) # Se ordena de mayor a menor
    soluciones = [] # Lista de monedas
    backtrack(cantidad, [], 0) # Llamada a la funcion de vuelta atrás
    if not soluciones: # Si la lista de monedas es vacía
        return "No se puede dar el cambio exacto con las monedas disponibles"
    return min(soluciones, key=len) # Retorna la lista de monedas con la longitud minima
monedas = [1, 5, 10, 50, 100, 500]  # Valores de las monedas en centavos
cantidad = 1523  # Cantidad deseada en centavos
# Prueba del algoritmo de vuelta atrás
print(f"Algoritmo de vuelta atrás: {cambio_monedas_backtracking(monedas, cantidad)}")

def min_coins(coins, amount):
    def backtrack(remaining_amount, coin_index, used_coins):
        if remaining_amount == 0:
            return len(used_coins)
        if coin_index == len(coins):
            return float('inf')
        
        min_coins = float('inf')
        current_coin = coins[coin_index]
        max_usage = remaining_amount // current_coin
        
        for i in range(max_usage, -1, -1):
            coins_used = used_coins + [current_coin]*i
            coins_required = backtrack(remaining_amount - i*current_coin, coin_index + 1, coins_used)
            min_coins = min(min_coins, coins_required)
        
        return min_coins
    
    coins.sort(reverse=True)  # sort coins in descending order
    min_coins_needed = backtrack(amount, 0, [])
    
    return min_coins_needed

# Ejemplo de uso
coins = [1, 5, 10, 50, 100, 500]  # Valores de las monedas en centavos
amount = 1523  # Cantidad deseada en centavos

min_coins_needed = min_coins(coins, amount)
print(f"El número mínimo de monedas necesarias es: {min_coins_needed}")