def coin_change(coins, amount):
    def estimate(coins, amount):
        return amount // coins[-1]

    def branch_and_bound(coins, amount, current_sum, index, count):
        nonlocal result

        if current_sum == amount:
            result = min(result, count)
            return

        if index == len(coins):
            return

        coin = coins[index]
        max_coins = (amount - current_sum) // coin
        for i in range(max_coins, -1, -1):
            if count + i < result:
                branch_and_bound(coins, amount, current_sum + i * coin, index + 1, count + i)

    coins.sort(reverse=True)
    result = float('inf')
    branch_and_bound(coins, amount, 0, 0, 0)
    return result

# Definir el conjunto de monedas chilenas y la cantidad deseada
coins = [500, 100, 50, 10, 5, 1]
amount = 2000

# Encontrar el número mínimo de monedas usando Ramificación y Poda
min_coins = coin_change(coins, amount)
print("Número mínimo de monedas necesarias:", min_coins)
monedas = [500, 100, 50, 10, 5, 1]
cantidad = 2000
# Prueba de ramificación y poda
print(f"Ramificación y Poda: {coin_change(monedas, cantidad)}")
