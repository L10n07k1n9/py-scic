import random
import scic as s

# Problemas

# Definir los campos que debería contener un documento que almacena los datos de un experimiento, por ejemplo, tiempo, temperatura, densidad, etc.
def define_col(file_nameseed=200):
    temp_col = "Tiempo"
    dilatacion_col = "Temp"
    densidad_col = "Densidad"

    header = [temp_col,dilatacion_col,densidad_col]

    mat = [header]
    for i in range(seed):
        mat.append(random.sample(range(0, 200), 4))
    s.save_matrix_csv(file_name, mat)
    return header
# Crear una colección llamada experimentos con al menos 200 experimentos aleatorios.

# Recuperar todos los experimentos y guardarlos en un archivo de texto con la siguiente estructura, por ejemplo, si los campos de cada experimento son: tiempo, temperatura, densidad, se debería construir el archivo:

# TIEMPO: 5 MIN
# TEMPERATURA: 127 C
# DENSIDAD: 5.2 U
# -------------------------------
# TIEMPO: 10 MIN
# TEMPERATURA: 58 C
# DENSIDAD: 6.2 U
# -------------------------------
# TIEMPO: 15 MIN
# TEMPERATURA: 69 C
# DENSIDAD: 3.1 U
# -------------------------------
# ...
# Crear un programa que recupere los datos del archivo anterior y los guarde en la colección experimentos_recuperados.
