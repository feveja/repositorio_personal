# Problema del cambio de monedas utilizando ramificación y poda (branch and bound)

class Node:
    # level: Número de monedas que se pueden usar
    # num_coins: Número de monedas que se han usado
    # remaining_amount: Cantidad restante
    def __init__(self, level, num_coins, remaining_amount): 
        self.level = level
        self.num_coins = num_coins
        self.remaining_amount = remaining_amount
# Cota inferior
def bound(node, coins, amount): # Cota inferior
    if node.remaining_amount == 0: # Si la cantidad restante es 0
        return node.num_coins 
    if node.remaining_amount < 0: # Si la cantidad restante es negativa
        return float('inf')
    total = node.num_coins # Número de monedas que se han usado
    i = node.level # Número de monedas que se pueden usar
    while i < len(coins) and node.remaining_amount > 0: # Mientras no se hayan usado todas las monedas y la cantidad restante sea mayor que 0
        total += node.remaining_amount // coins[i] # Número de monedas de este tipo que se pueden usar
        node.remaining_amount %= coins[i] # Reducir la cantidad restante por el valor usado
        i += 1 # Pasar a la moneda siguiente
    return total # Retorna el número de monedas que se han usado

def coin_change_branch_and_bound(coins, amount): # Ramificar y podar
    coins.sort(reverse=True) # Se ordena de mayor a menor
    Q = [] # Cola de nodos
    root = Node(0, 0, amount) # Raíz
    Q.append(root) # Agregar la raíz a la cola de nodos
    min_coins = float('inf') # Cota inferior
    
    while Q: # Mientras la cola de nodos no este vacía
        node = Q.pop(0) # Obtener el primer nodo de la cola de nodos
        
        if node.remaining_amount == 0: # Si la cantidad restante es 0
            min_coins = min(min_coins, node.num_coins) # Actualizar la cota inferior
            continue
        
        if node.level == len(coins):
            continue
        
        # No tomar la moneda actual
        not_take = Node(node.level + 1, node.num_coins, node.remaining_amount)
        if bound(not_take, coins, amount) < min_coins:
            Q.append(not_take)
        
        # Tomar la moneda actual
        take = Node(node.level, node.num_coins + 1, node.remaining_amount - coins[node.level])
        if bound(take, coins, amount) < min_coins:
            Q.append(take)
    
    return min_coins if min_coins != float('inf') else -1

# Pruebas
coins = [1, 2, 5]
amount = 11

print(coin_change_branch_and_bound(coins, amount))  # Salida: 3

coins = [2]
amount = 3

print(coin_change_branch_and_bound(coins, amount))  # Salida: -1

coins = [1]
amount = 0

print(coin_change_branch_and_bound(coins, amount))  # Salida: 0

