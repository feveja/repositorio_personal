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
print(f"Algoritmo de vuelta atrás: {cambio_monedas_backtracking(monedas, cantidad)}")