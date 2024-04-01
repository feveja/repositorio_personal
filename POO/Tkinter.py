import tkinter as tk

def actualizar_etiqueta():
    etiqueta.config(text="¡Hola, Tkinter!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo Tkinter")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Bienvenido a Tkinter")
etiqueta.pack(pady=10)

# Crear un botón
boton = tk.Button(ventana, text="Actualizar etiqueta", command=actualizar_etiqueta)
boton.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
