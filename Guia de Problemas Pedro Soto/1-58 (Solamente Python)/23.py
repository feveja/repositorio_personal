# Pedir un número al usuario
num = int(input("Introduce un número: "))

# Mostrar el número en formato exponencial
exp = ""
if num < 0:
    exp = "-"
    num = -num
if num >= 10:
    exp += str(num // 10) + " * ^10"
    num %= 10
if num > 0:
    exp += str(num) + "^1"
print(exp)