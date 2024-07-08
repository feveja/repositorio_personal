# Problema del cambio de monedas utilizando programación dinámica
# coins: lista de monedas
# amount: cantidad a cambiar
def coin_change_dynamic_programming(coins, amount): 
    dp = [float('inf')] * (amount + 1) # Crear una tabla para almacenar los valores mínimos
    dp[0] = 0 # El valor 0 es 0
    
    for coin in coins: # Por cada moneda
        for x in range(coin, amount + 1): # Por cada cantidad
            dp[x] = min(dp[x], dp[x - coin] + 1) # Actualizar la tabla de abajo hacia arriba
    
    return dp[amount] if dp[amount] != float('inf') else -1 # Retornar el valor máximo

# Pruebas
coins = [1, 2, 5]
amount = 11

print(coin_change_dynamic_programming(coins, amount))  # Salida: 3

coins = [2]
amount = 3

print(coin_change_dynamic_programming(coins, amount))  # Salida: -1

coins = [1]
amount = 0

print(coin_change_dynamic_programming(coins, amount))  # Salida: 0
