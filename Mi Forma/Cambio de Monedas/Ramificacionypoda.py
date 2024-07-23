def coin_change(coins, amount):
    # Estimación de la cantidad mínima de monedas (no utilizada en el algoritmo)
    def estimate(coins, amount):
        return amount // coins[-1]

    # Función principal de Ramificación y Poda
    def branch_and_bound(coins, amount, current_sum, index, count):
        nonlocal result

        # Si la suma actual es igual al monto deseado, actualizar el resultado mínimo
        if current_sum == amount:
            result = min(result, count)
            return

        # Si el índice ha alcanzado la longitud de la lista de monedas, retornar
        if index == len(coins):
            return

        coin = coins[index]
        # Calcular la cantidad máxima de monedas de este valor que se pueden usar
        max_coins = (amount - current_sum) // coin
        for i in range(max_coins, -1, -1):
            # Poda: si el conteo actual más la cantidad de monedas consideradas es menor que el resultado
            if count + i < result:
                branch_and_bound(coins, amount, current_sum + i * coin, index + 1, count + i)

    # Ordenar las monedas en orden descendente
    coins.sort(reverse=True)
    result = float('inf')
    # Llamar a la función de Ramificación y Poda
    branch_and_bound(coins, amount, 0, 0, 0)
    return result

# Definir el conjunto de monedas y la cantidad deseada
coins = [500, 100, 50, 10, 5, 1]
amount = 2000

# Encontrar el número mínimo de monedas usando Ramificación y Poda
min_coins = coin_change(coins, amount)
print("Número mínimo de monedas necesarias:", min_coins)

# Prueba de ramificación y poda
print(f"Ramificación y Poda: {coin_change(coins, amount)}")
