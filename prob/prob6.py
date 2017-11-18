import scic as s
import random
import matplotlib.pyplot as plt
from collections import Counter
# Problemas

# Generar un archivo CSV con valores aleatorios que almacene los datos de un experimento ficticio que consta de los campos Tiempo, Dilatacion, Temperatura, Densidad.
file_name = "prob6.csv"
temp_col = "Temperatura"
dilatacion_col = "Dilatacion"
temp_validation = "Invalido"
dilatacion_validation = "Sobredilatado"
header = ["Tiempo", dilatacion_col, "Temperatura", "Densidad"]
mat = [header]
for i in range(1000 + 1):
    mat.append(random.sample(range(0, 200), 4))
s.save_matrix_csv(file_name, mat)
# Cargar los datos con la función scic.load_data_csv(...) e imprimirlos.
data, x = s.open_csv_metadata(file_name), 0
while x < len(data["data"]["rows"]):
    el = data["data"]["rows"][x]
    # Generar el dato categórico Invalido el cual se determina si la temperatura es mayor a 60 (SI o NO).
    if int(el[temp_col], 10) > 60:
        el[temp_validation] = "SI"
    else:
        el[temp_validation] = "NO"
    # Generar el dato categórico Sobredilatado el cual se determina si la dilatación es mayor a 4.
    if int(el[dilatacion_col], 10) > 4:
        el[dilatacion_validation] = "SI"
    else:
        el[dilatacion_validation] = "NO"
    x = x + 1

# Graficar la columna Invalido y la columna Sobredilatado en dos gráficas de pastel (en ventanas distintas).
# Invalid plot
labels_invalid_temp = list(
    map(lambda item: item[temp_validation], data["data"]["rows"]))
count_labels_invalid_temp = Counter(labels_invalid_temp)
labels1, sizes1 = count_labels_invalid_temp.keys(), count_labels_invalid_temp.values()

fig1, axis1 = plt.subplots()
axis1.pie(sizes1, explode=None, labels=labels1,
          autopct='%1.1f%%', shadow=True, startangle=40)

axis1.axis('equal')

# Sobredilatado
labels_invalid_dil = list(
    map(lambda item: item[dilatacion_validation], data["data"]["rows"]))
count_labels_invalid_dil = Counter(labels_invalid_dil)
labels2, sizes2 = count_labels_invalid_dil.keys(), count_labels_invalid_dil.values()

fig2, axis2 = plt.subplots()
axis2.pie(sizes2, explode=None, labels=labels2,
          autopct='%1.1f%%', shadow=True, startangle=40)

axis2.axis('equal')

plt.show()
