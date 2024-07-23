import tkinter as tk
from tkinter import ttk

# Algoritmo de ramificación y poda para la mochila 0/1
def branch_and_bound_knapsack(values, weights, capacity, update_ui=None):
    n = len(values)
    indices = list(range(n))
    
    def upper_bound(curr_weight, curr_value, k):
        upper_bound_value = curr_value
        upper_bound_weight = curr_weight
        
        while k < n and upper_bound_weight + weights[indices[k]] <= capacity:
            upper_bound_weight += weights[indices[k]]
            upper_bound_value += values[indices[k]]
            k += 1
        
        if k < n:
            upper_bound_value += (capacity - upper_bound_weight) * values[indices[k]] / weights[indices[k]]
        
        return upper_bound_value
    
    def lower_bound(curr_weight, curr_value, k):
        lower_bound_value = curr_value
        lower_bound_weight = curr_weight
        
        for i in range(k, n):
            if lower_bound_weight + weights[indices[i]] <= capacity:
                lower_bound_weight += weights[indices[i]]
                lower_bound_value += values[indices[i]]
            else:
                remaining_capacity = capacity - lower_bound_weight
                lower_bound_value += values[indices[i]] * (remaining_capacity / weights[indices[i]])
                break
        
        return lower_bound_value
    
    def knapsack_recursive(curr_weight, curr_value, k):
        nonlocal max_value
        nonlocal best_set
        if curr_weight <= capacity and curr_value > max_value:
            max_value = curr_value
            best_set = set(indices[:k])
            if update_ui:
                update_ui(curr_weight, curr_value, k, "update_best")

        if k == n:
            return
        
        if upper_bound(curr_weight, curr_value, k) <= max_value:
            return
        
        if lower_bound(curr_weight, curr_value, k) > max_value:
            if update_ui:
                update_ui(curr_weight + weights[indices[k]], curr_value + values[indices[k]], k + 1, "include")
            knapsack_recursive(curr_weight + weights[indices[k]], curr_value + values[indices[k]], k + 1)
        
        if update_ui:
            update_ui(curr_weight, curr_value, k + 1, "exclude")
        knapsack_recursive(curr_weight, curr_value, k + 1)
    
    max_value = 0
    best_set = set()
    knapsack_recursive(0, 0, 0)
    
    return max_value, best_set

# Función para actualizar la interfaz gráfica
def update_ui(curr_weight, curr_value, k, action):
    status_text.set(f"Peso actual: {curr_weight}, Valor actual: {curr_value}, Índice: {k}, Acción: {action}")
    root.update_idletasks()

# Crear la ventana principal
root = tk.Tk()
root.title("Visualización de Ramificación y Poda")

# Crear y configurar los widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

status_text = tk.StringVar()
status_label = ttk.Label(frame, textvariable=status_text, padding="10")
status_label.grid(row=0, column=0, columnspan=2)

start_button = ttk.Button(frame, text="Iniciar Algoritmo", command=lambda: branch_and_bound_knapsack(
    values=[60, 100, 120],
    weights=[10, 20, 30],
    capacity=50,
    update_ui=update_ui
))
start_button.grid(row=1, column=0, columnspan=2)

# Iniciar el bucle principal de la interfaz
root.mainloop()
