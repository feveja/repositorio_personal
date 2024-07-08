# Problema 11: Suma de los dígitos de un número ingresado como un número

# Ingresar el número
numero = int(input("Ingresa un número de n dígitos: "))

# Convertir el número a una cadena para poder iterar sobre sus dígitos
numero_str = str(numero)

# Inicializar la suma
suma_digitos = 0

# Sumar los dígitos
for digito in numero_str:
    suma_digitos = suma_digitos + int(digito)

# Mostrar la suma de los dígitos
print("La suma de los dígitos es: ",suma_digitos)
