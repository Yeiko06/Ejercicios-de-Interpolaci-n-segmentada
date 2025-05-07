import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos del vehículo
x = np.array([40, 60, 80, 100, 120, 140])
y = np.array([6.5, 5.8, 5.5, 5.7, 6.2, 7.0])

# Interpolaciones
lineal = interp1d(x, y, kind='linear')
cuadratica = interp1d(x, y, kind='quadratic')
cubica = interp1d(x, y, kind='cubic')

# Nuevos puntos para graficar
x_vals = np.linspace(40, 140, 300)
y_lineal = lineal(x_vals)
y_cuadratica = cuadratica(x_vals)
y_cubica = cubica(x_vals)

# Gráfica
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', label='Datos originales')
plt.plot(x_vals, y_lineal, '--', label='Interpolación Lineal', color='blue')
plt.plot(x_vals, y_cuadratica, '-.', label='Interpolación Cuadrática', color='green')
plt.plot(x_vals, y_cubica, label='Interpolación Cúbica', color='purple')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Consumo (L/100 km)')
plt.title('Interpolación Segmentada - Consumo de Combustible')
plt.legend()
plt.grid()
plt.savefig('consumo_interpolacion.png')
plt.show()
