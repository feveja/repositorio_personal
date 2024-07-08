# Programa para calcular la raíz cuadrada de un número
numero = float(input("Introduce un número: "))

if numero >= 0:
    # Calculo de la raíz cuadrada utilizando el método de aproximación (método de babilonia)
    x = numero
    y = 1
    e = 0.000001  # margen de error
    while (x - y > e):
        x = (x + y) / 2
        y = numero / x
    print("La raíz cuadrada de", numero, "es", x)
else:
    print("Raíz imaginaria")
    print("Valor:", numero)
