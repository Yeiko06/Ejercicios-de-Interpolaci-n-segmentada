import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de la viga
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, -1.5, -2.8, -3.0, -2.7, -2.0])

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
plt.xlabel('Longitud (m)')
plt.ylabel('Deflexión (mm)')
plt.title('Interpolación Segmentada - Deflexión de una Viga')
plt.legend()
plt.grid()
plt.savefig('viga_interpolacion.png')
plt.show()
