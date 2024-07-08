def hanoi_iterativo(n, origen, destino, auxiliar):
    # Número total de movimientos necesarios
    total_movimientos = 2**n - 1

    # Identificación de las varillas
    varillas = [origen, destino, auxiliar]

    # Si el número de discos es par, intercambiar el destino y el auxiliar
    if n % 2 == 0:
        destino, auxiliar = auxiliar, destino

    # Inicializar las pilas para las varillas
    varillas_pilas = {origen: list(range(n, 0, -1)), destino: [], auxiliar: []}

    for i in range(1, total_movimientos + 1):
        if i % 3 == 1:
            mover(varillas_pilas, origen, destino)
        elif i % 3 == 2:
            mover(varillas_pilas, origen, auxiliar)
        elif i % 3 == 0:
            mover(varillas_pilas, auxiliar, destino)

def mover(varillas_pilas, fuente, destino):
    if not varillas_pilas[fuente]:
        disco = varillas_pilas[destino].pop()
        varillas_pilas[fuente].append(disco)
        print(f"Mover disco {disco} desde {destino} hasta {fuente}")
    elif not varillas_pilas[destino]:
        disco = varillas_pilas[fuente].pop()
        varillas_pilas[destino].append(disco)
        print(f"Mover disco {disco} desde {fuente} hasta {destino}")
    elif varillas_pilas[fuente][-1] > varillas_pilas[destino][-1]:
        disco = varillas_pilas[destino].pop()
        varillas_pilas[fuente].append(disco)
        print(f"Mover disco {disco} desde {destino} hasta {fuente}")
    else:
        disco = varillas_pilas[fuente].pop()
        varillas_pilas[destino].append(disco)
        print(f"Mover disco {disco} desde {fuente} hasta {destino}")

# Ejemplo de uso
n = 74  # Número de discos
hanoi_iterativo(n, 'A', 'C', 'B')
