n = int(input("Ingrese el número base: "))
m = int(input("Ingrese el número límite: "))

for i in range(n, m + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()
