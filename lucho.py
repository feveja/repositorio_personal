import tkinter as tk

# Paso 1: Definir la estructura del grafo
grafo = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': []
}

# Paso 2: Implementar la función para mostrar el recorrido del grafo
def recorrer_grafo(grafo, inicio, destino):
    cola = [(inicio,)]
    visitados = set()

    while cola:
        camino = cola.pop(0)
        ultimo_vertice = camino[-1]

        if ultimo_vertice == destino:
            return camino

        if ultimo_vertice not in visitados:
            visitados.add(ultimo_vertice)
            for vecino in grafo[ultimo_vertice]:
                nuevo_camino = camino + (vecino,)
                cola.append(nuevo_camino)

    return None

# Paso 3: Crear la interfaz gráfica
def mostrar_recorrido():
    inicio = entrada_inicio.get().upper()
    destino = entrada_fin.get().upper()
    if inicio in grafo and destino in grafo:
        camino = recorrer_grafo(grafo, inicio, destino)
        if camino:
            recorrido_text.delete('1.0', tk.END)
            for i in range(len(camino) - 1):
                recorrido_text.insert(tk.END, f"{i+1}) {camino[i]} -> {camino[i+1]}\n")
        else:
            recorrido_text.delete('1.0', tk.END)
            recorrido_text.insert(tk.END, "No se encontró un camino entre los vértices.")
    else:
        recorrido_text.delete('1.0', tk.END)
        recorrido_text.insert(tk.END, "Vértices no válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Grafos Dirigidos")

# Crear y ubicar los widgets
tk.Label(root, text="Vértice de inicio:").pack()
entrada_inicio = tk.Entry(root)
entrada_inicio.pack()

tk.Label(root, text="Vértice de fin:").pack()
entrada_fin = tk.Entry(root)
entrada_fin.pack()

tk.Button(root, text="Mostrar Recorrido", command=mostrar_recorrido).pack()

recorrido_label = tk.Label(root, text="Recorrido del Grafo:")
recorrido_label.pack()

recorrido_text = tk.Text(root, height=10, width=50)
recorrido_text.pack()

# Iniciar el bucle de la aplicación
root.mainloop()
