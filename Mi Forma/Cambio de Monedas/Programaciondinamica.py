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

# Prueba de la programación dinámica
print(f"Programación Dinámica: {cambio_monedas_dp(monedas, cantidad)}")
