import scic as s
import random
# Problemas

# Generar un archivo CSV con valores aleatorios que almacene los datos de un experimento ficticio que consta de los campos Tiempo, Dilatacion, Temperatura, Densidad.
file_name = "prob6.csv"
temp_col = "Temperatura"
header = ["Tiempo", "Dilatacion", "Temperatura", "Densidad"]
mat = [header]
for i in range(1000 + 1):
    mat.append(random.sample(range(0, 200), 4))
s.save_matrix_csv(file_name, mat)
# Cargar los datos con la función scic.load_data_csv(...) e imprimirlos.
data = s.load_matrix_csv(file_name)
temp = data[temp_col]
# Generar el dato categórico Invalido el cual se determina si la temperatura es mayor a 60 (SI o NO).
cat_invalido = map(lambda x: x > 60, temp)
# Generar el dato categórico Sobredilatado el cual se determina si la dilatación es mayor a 4.

# Graficar la columna Invalido y la columna Sobredilatado en dos gráficas de pastel (en ventanas distintas).
