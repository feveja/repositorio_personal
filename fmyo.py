import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda
amplitud = 0.06
fase_inicial = 0
longitud_onda = 2 * np.pi / 0.02
periodo = 2 * np.pi / 4

# Generar arrays para x y t
x = np.linspace(0, 1, 500)
t = np.linspace(0,200, 500)

# Generar la onda
onda = amplitud * np.sin(0.02 * np.pi * x - 4 * np.pi * t)

# Graficar onda vs tiempo
plt.figure(figsize=(12, 6))
plt.subplot(1,2,1)
plt.plot(t, onda)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Onda vs Tiempo')
plt.grid(True)

# Graficar onda vs longitud del medio
plt.subplot(1,2,2)
plt.plot(x, onda)
plt.xlabel('Longitud del medio')
plt.ylabel('Amplitud')
plt.title('Onda vs Longitud del medio')
plt.grid(True)

plt.tight_layout()
plt.show()