# Programa EsLetra
caracter = input("Introduce un carácter: ")

es_letra = 0  # Inicialmente asumimos que no es una letra

# Verificar mayúsculas
for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if caracter == letra:
        es_letra = 1
        break

# Verificar minúsculas
if es_letra == 0:  # Solo verificar minúsculas si no es mayúscula
    for letra in 'abcdefghijklmnopqrstuvwxyz':
        if caracter == letra:
            es_letra = 1
            break

print(es_letra)