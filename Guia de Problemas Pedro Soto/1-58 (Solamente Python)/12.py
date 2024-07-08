# Problema 12: Suma de los dígitos de un número ingresado como palabra

# Ingresar el número como una palabra
numero_palabra = input("Ingresa un número de n dígitos (almacénalo como palabra): ")

# Inicializar la suma
suma_digitos = 0

# Sumar los dígitos
for digito in numero_palabra:
    suma_digitos = suma_digitos + int(digito)

# Mostrar la suma de los dígitos
print("La suma de los dígitos es: ",suma_digitos)
