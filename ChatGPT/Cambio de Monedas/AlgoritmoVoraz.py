# Problema del cambio de monedas utilizando un enfoque voraz (Greedy)

def coin_change_greedy(coins, amount):
    # Ordenar las monedas en orden descendente
    coins.sort(reverse=True) # Se ordena de mayor a menor
    num_coins = 0 # Número de monedas que se pueden usar
    
    for coin in coins: # Por cada moneda
        if amount >= coin: # Si la cantidad total es mayor o igual que el valor de la moneda
            num_coins += amount // coin  # Número de monedas de este tipo que se pueden usar
            amount %= coin  # Reducir la cantidad total por el valor usado

    # Si después de usar todas las monedas no se puede completar la cantidad, retornar -1
    return num_coins if amount == 0 else -1

# Pruebas
coins = [1, 2, 5]
amount = 11
print(coin_change_greedy(coins, amount))  # Salida esperada: 3 (óptima en este caso)

coins = [2]
amount = 3
print(coin_change_greedy(coins, amount))  # Salida esperada: -1 (no se puede completar la cantidad)

coins = [1, 5, 10, 25]
amount = 30
print(coin_change_greedy(coins, amount))  # Salida esperada: 2 (óptima en este caso)
