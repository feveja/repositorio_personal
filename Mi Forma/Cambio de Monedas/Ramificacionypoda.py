import heapq

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
print(f"Ramificación y Poda: {cambio_monedas_branch_and_bound(monedas, cantidad)}")
