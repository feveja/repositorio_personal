def combinatoria(n, k):
    # Casos base
    if k == 0 or k == n:
        return 1
    # Llamada recursiva utilizando la propiedad combinatoria
    return combinatoria(n - 1, k - 1) + combinatoria(n - 1, k)

# Ejemplo de uso
n = 5
k = 2
resultado = combinatoria(n, k)
print(f"C({n}, {k}) = {resultado}")
