import numpy as np
import matplotlib.pyplot as plt

# Datos
ℓ = 2  # Longitud de la cuerda en metros
θ = np.pi / 16  # Ángulo en radianes
ω_0 = np.pi / 8  # Velocidad angular inicial en rad/s
g = 9.8  # Aceleración debida a la gravedad en m/s^2

# Calculando la amplitud
A = ℓ * θ

# Calculando el periodo
T = 2 * np.pi * np.sqrt(ℓ / g)

# Calculando la fase inicial
φ = np.arcsin(A / ℓ)

# Definición de la función de posición angular θ en función del tiempo t
def theta(t):
    return A * np.sin(np.sqrt(g / ℓ) * t + φ)

# Generando valores de tiempo para el gráfico
t_values = np.linspace(0, 3 * T, 1000)

# Generando valores de posición angular θ en función del tiempo t
θ_values = theta(t_values)

# Graficando
plt.plot(t_values, θ_values, label='Posición angular θ vs tiempo t')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición angular (rad)')
plt.title('Gráfico de posición angular vs tiempo')
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)  # Línea horizontal en y=0
plt.axvline(x=0, color='k', linestyle='--', linewidth=0.5)  # Línea vertical en x=0
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# Mostrando los resultados
print(f'Amplitud (A): {A:.2f} m')
print(f'Fase inicial (φ): {np.degrees(φ):.2f} grados')
print(f'Periodo (T): {T:.2f} s')
