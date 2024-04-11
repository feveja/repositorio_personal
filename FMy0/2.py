import numpy as np
import matplotlib.pyplot as plt

# Constantes
g = 9.8  # m/s^2
R = 2    # m

# Amplitud y fase inicial
A = np.pi / 8
phi = 0

# Frecuencia angular y periodo
omega = np.sqrt(g / R)
T = 2 * np.pi / omega

# Tiempo
t = np.linspace(0, 5*T, 1000)

# Posición angular en función del tiempo
theta = A * np.sin(omega * t + phi)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, theta, label='Posición angular')
plt.title('Posición Angular vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición Angular (rad)')
plt.grid(True)
plt.legend()
plt.show()
