#Problema de cambio de monedas utilizando un enfoque voraz (Greedy)
#https://youtu.be/Yn7HUks2ju8?si=GcefJFaAxXE_s7k_
#Cambios: Sacamos la moneda de la lista de monedas de la funcion y la llamamos desde afuera
def cambio_monedas_greedy(monedas, cantidad):
    # Ordenamos las monedas en orden descendente
    monedas.sort(reverse=True) 
    resultado = []
    for moneda in monedas: # Recorremos todas las monedas
        while cantidad >= moneda: # Si la cantidad es mayor o igual a la moneda
            cantidad -= moneda # Disminuimos la cantidad
            resultado.append(moneda) # Agregamos la moneda al resultado
    if cantidad != 0: # Si la cantidad no es 0
        return "No se puede dar el cambio exacto con las monedas disponibles"
    return resultado # Retornamos el resultado

# Prueba del algoritmo voraz
monedas = [500, 100, 50, 10, 5, 1]
cantidad = 2000
print(f"Algoritmo Voraz: {cambio_monedas_greedy(monedas, cantidad)}")
