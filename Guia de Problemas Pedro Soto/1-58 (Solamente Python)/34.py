# Programa llamado EsDigito
caracter = input("Introduce un carácter: ")

es_digito = 0
for digito in '0123456789':
    if caracter == digito:
        es_digito = 1
        break

print(es_digito)
