## Dibjar una gráfica de valores X y Y

# La gráfica más sencilla es aquella que grafica puntos X y Y, para lograrlo deberemos proporcionar la lista de valores en X y la lista de valores en Y. Luego mediante la función plot podremos graficar y mostrar la gráfica. Ejecuta el siguiente código y analizalo:

import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])

# plt.show()
## Ajustar el color y tipo de la gráfica

# Podemos especificar el color de gráfica mediante la primer letra del color en inglés y el tipo de gráfica mediante un caracter, por ejemplo, r* muestra asteríscos de color rojo, k- muestra una línea consecutiva de color negro, b+ muestra símbolos + de color azul.
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'g--')

plt.show()

# Podemos establecer varias gráficas en una sola mediante subplots indicando cuántas filas y columnas deseamos mostrar. El método subplots siempre devuelve la figura y una matriz de axis, cada axis nos permitirá dibujar una gráfica independiente:
fig, axis = plt.subplots(3, 2)

axis[0, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'r+')
axis[0, 1].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'b*')

axis[1, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'g+')
axis[1, 1].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'y*')

axis[2, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'k+')
axis[2, 1].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'r-')

plt.show()