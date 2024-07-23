#Cambio de Monedas Programación Dinámica
def cambio_monedas_dp(monedas, cantidad): 
    max_valor = float('inf') # Crear una tabla para almacenar los valores mínimos
    dp = [0] + [max_valor] * cantidad # Llenar la tabla de abajo hacia arriba
    for i in range(1, cantidad + 1): # Por cada moneda
        for moneda in monedas: # Por cada cantidad
            if i >= moneda: # Si la cantidad es mayor o igual a la moneda
                dp[i] = min(dp[i], dp[i - moneda] + 1) # Actualizar la tabla de abajo hacia arriba
    if dp[cantidad] == max_valor: # Si la tabla no se puede dar el cambio exacto con las monedas disponibles
        return "No se puede dar el cambio exacto con las monedas disponibles"
    resultado = [] # Crear una lista para almacenar el resultado
    while cantidad > 0: # Por cada moneda
        for moneda in monedas: # Por cada cantidad
            if cantidad >= moneda and dp[cantidad] == dp[cantidad - moneda] + 1: # Si la cantidad es mayor o igual a la moneda y el valor de la tabla es igual al valor de la tabla menos la moneda
                resultado.append(moneda) # Agregar la moneda al resultado
                cantidad -= moneda # Disminuir la cantidad
                break # Romper el bucle
    return resultado # Devolver el resultado
monedas = [500, 100, 50, 10, 5, 1]
cantidad = 2000
# Prueba de la programación dinámica
print(f"Programación Dinámica: {cambio_monedas_dp(monedas, cantidad)}")
