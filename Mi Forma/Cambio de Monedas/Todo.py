import heapq,time,tracemalloc
def cambio_monedas_greedy(monedas, cantidad):
    # Ordenamos las monedas en orden descendente
    monedas.sort(reverse=True)
    resultado = []
    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            resultado.append(moneda)
    if cantidad != 0:
        return "No se puede dar el cambio exacto con las monedas disponibles"
    return resultado
monedas = [500, 100, 50, 10, 5, 1]
cantidad = 879
print(f"Algoritmo Voraz: {cambio_monedas_greedy(monedas, cantidad)}")

def cambio_monedas_dp(monedas, cantidad):
    max_valor = float('inf')
    dp = [0] + [max_valor] * cantidad
    for i in range(1, cantidad + 1):
        for moneda in monedas:
            if i >= moneda:
                dp[i] = min(dp[i], dp[i - moneda] + 1)
    if dp[cantidad] == max_valor:
        return "No se puede dar el cambio exacto con las monedas disponibles"
    resultado = []
    while cantidad > 0:
        for moneda in monedas:
            if cantidad >= moneda and dp[cantidad] == dp[cantidad - moneda] + 1:
                resultado.append(moneda)
                cantidad -= moneda
                break
    return resultado
monedas = [500, 100, 50, 10, 5, 1]
cantidad = 879
# Prueba de la programación dinámica
print(f"Programación Dinámica: {cambio_monedas_dp(monedas, cantidad)}")

def cambio_monedas_backtracking(monedas, cantidad):
    def backtrack(remain, path, index):
        if remain == 0:
            soluciones.append(path)
            return
        for i in range(index, len(monedas)):
            if monedas[i] <= remain:
                backtrack(remain - monedas[i], path + [monedas[i]], i)
    
    monedas.sort(reverse=True)
    soluciones = []
    backtrack(cantidad, [], 0)
    if not soluciones:
        return "No se puede dar el cambio exacto con las monedas disponibles"
    return min(soluciones, key=len)

# Prueba del algoritmo de vuelta atrás
monedas = [500, 100, 50, 10, 5, 1]
cantidad = 879
print(f"Vuelta Atrás: {cambio_monedas_backtracking(monedas, cantidad)}")

def cambio_monedas_branch_and_bound(monedas, cantidad):
    class Nodo:
        def __init__(self, nivel, acumulado, restante, camino):
            self.nivel = nivel
            self.acumulado = acumulado
            self.restante = restante
            self.camino = camino
        def __lt__(self, otro):
            return self.restante < otro.restante

    def bound(nodo):
        if nodo.restante == 0:
            return nodo.acumulado
        for moneda in monedas[nodo.nivel:]:
            if nodo.restante >= moneda:
                nodo.restante -= moneda
                nodo.acumulado += 1
            if nodo.restante == 0:
                break
        return nodo.acumulado

    monedas.sort(reverse=True)
    nodo_inicial = Nodo(0, 0, cantidad, [])
    cola = [nodo_inicial]
    heapq.heapify(cola)
    min_acumulado = float('inf')
    mejor_camino = []

    while cola:
        nodo_actual = heapq.heappop(cola)
        if nodo_actual.restante == 0:
            if nodo_actual.acumulado < min_acumulado:
                min_acumulado = nodo_actual.acumulado
                mejor_camino = nodo_actual.camino
        elif nodo_actual.nivel < len(monedas):
            for i in range(nodo_actual.nivel, len(monedas)):
                nueva_restante = nodo_actual.restante - monedas[i]
                if nueva_restante >= 0:
                    nuevo_nodo = Nodo(i, nodo_actual.acumulado + 1, nueva_restante, nodo_actual.camino + [monedas[i]])
                    if nuevo_nodo.acumulado + nueva_restante // monedas[i] < min_acumulado:
                        heapq.heappush(cola, nuevo_nodo)
    if not mejor_camino:
        return "No se puede dar el cambio exacto con las monedas disponibles"
    return mejor_camino

# Prueba de ramificación y poda
monedas = [500, 100, 50, 10, 5, 1]
cantidad = 879
print(f"Ramificación y Poda: {cambio_monedas_branch_and_bound(monedas, cantidad)}")


# Función para ejecutar y medir rendimiento
def medir_rendimiento(func, *args):
    tracemalloc.start()
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tiempo = fin - inicio
    memoria_usada = memoria[1] - memoria[0]
    return resultado, tiempo, memoria_usada

# Datos de prueba
monedas = [500, 100, 50, 10, 5, 1]
cantidad = 879

# Algoritmos a probar
algoritmos = [
    ("Algoritmo Voraz", cambio_monedas_greedy),
    ("Programación Dinámica", cambio_monedas_dp),
    ("Vuelta Atrás", cambio_monedas_backtracking),
    ("Ramificación y Poda", cambio_monedas_branch_and_bound)
]

# Realizar pruebas
resultados = {}
for nombre, algoritmo in algoritmos:
    resultados[nombre] = []
    for _ in range(3):  # Tres ejecuciones
        resultado, tiempo, memoria = medir_rendimiento(algoritmo, monedas, cantidad)
        resultados[nombre].append((resultado, tiempo, memoria))

# Mostrar resultados
for nombre, valores in resultados.items():
    tiempos = [v[1] for v in valores]
    memorias = [v[2] for v in valores]
    print(f"{nombre}:")
    print(f"  Promedio de tiempo: {sum(tiempos) / len(tiempos):.6f} segundos")
    print(f"  Promedio de memoria: {sum(memorias) / len(memorias)} bytes")
    print()

medir_rendimiento(cambio_monedas_branch_and_bound, monedas, cantidad)
