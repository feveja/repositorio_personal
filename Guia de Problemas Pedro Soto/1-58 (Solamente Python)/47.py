# Programa para calcular el salario neto semanal

# Entrada de datos
nombre = input("Introduce el nombre del trabajador: ")
horas_trabajadas = int(input("Introduce el número de horas trabajadas: "))
tarifa_normal = float(input("Introduce la tarifa por hora: "))

# Calculo del salario bruto
if horas_trabajadas <= 40:
    salario_bruto = horas_trabajadas * tarifa_normal
else:
    salario_bruto = (40 * tarifa_normal) + ((horas_trabajadas - 40) * tarifa_normal * 1.5)

# Calculo de impuestos
impuestos = 0
salario_sujeto_a_impuestos = salario_bruto

if salario_sujeto_a_impuestos > 90:
    impuestos += (salario_sujeto_a_impuestos - 90) * 0.45
    salario_sujeto_a_impuestos = 90
if salario_sujeto_a_impuestos > 50:
    impuestos += (salario_sujeto_a_impuestos - 50) * 0.25
    salario_sujeto_a_impuestos = 50

# Salario neto
salario_neto = salario_bruto - impuestos

# Mostrar resultados sin usar round
print("Nombre:", nombre)
print("Salario bruto:", salario_bruto)
print("Impuestos:", impuestos)
print("Salario neto:", salario_neto)
