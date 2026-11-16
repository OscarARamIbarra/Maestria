
import numpy as np
import matplotlib.pyplot as plt

# Se definen los valores de x
x = np.linspace(-4, 8, 500)

# Aqui se define la función
f = x**2 - 4*x - 5

# Se grafica la función cuadrática
plt.plot(x, f, label='f(x) = x² - 4x - 5', color='blue')

# Se agregan los ejes coordenados
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Configuración de la gráfica
plt.title('Función cuadrática')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# Se muestra la gráfica
plt.show()