import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos del motor
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([250, 220, 180, 150, 130, 125])

# Interpolaciones
lineal = interp1d(x, y, kind='linear')
cuadratica = interp1d(x, y, kind='quadratic')
cubica = interp1d(x, y, kind='cubic')

# Nuevos puntos para graficar
x_vals = np.linspace(0, 5, 200)
y_lineal = lineal(x_vals)
y_cuadratica = cuadratica(x_vals)
y_cubica = cubica(x_vals)

# Gráfica
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', label='Datos originales')
plt.plot(x_vals, y_lineal, '--', label='Interpolación Lineal', color='blue')
plt.plot(x_vals, y_cuadratica, '-.', label='Interpolación Cuadrática', color='green')
plt.plot(x_vals, y_cubica, label='Interpolación Cúbica', color='purple')
plt.xlabel('Distancia (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Interpolación Segmentada - Temperatura en el Motor')
plt.legend()
plt.grid()
plt.savefig('motor_interpolacion.png')
plt.show()
