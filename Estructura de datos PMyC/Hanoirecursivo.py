def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 desde {origen} hasta {destino}")
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} desde {origen} hasta {destino}")
        hanoi(n - 1, auxiliar, destino, origen)

# Ejemplo de uso
n = 20  # Número de discos
hanoi(n, 'A', 'C', 'B')
