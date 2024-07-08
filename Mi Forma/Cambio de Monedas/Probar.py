import time
import tracemalloc

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
