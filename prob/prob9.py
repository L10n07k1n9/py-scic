import re
import random
import scic as s
import sys
import pymongo
from pymongo import MongoClient
# Problemas
file_name = "./prob/prob9.csv"
time_col = "TIEMPO"
tem_col = "TEMPERATURA"
densidad_col = "DENSIDAD"
# Definir los campos que debería contener un documento que almacena los datos de un experimiento, por ejemplo, tiempo, temperatura, densidad, etc.


def define_col(seed=200):

    header = [time_col, tem_col, densidad_col]

    mat = [header]
    for i in range(seed):
        mat.append(random.sample(range(0, 200), 3))
    return s.save_matrix_csv(file_name, mat)



# Crear una colección llamada experimentos con al menos 200 experimentos aleatorios.
define_col()

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
data, x, file_format, file_txt_formatted, separator = s.open_csv_metadata(
    file_name), 0, [], file_name + ".txt", "-------------------------------"
file_format = list(map(lambda row: "TIEMPO: {} MIN\nTEMPERATURA: {} C\nDENSIDAD: {} U\n{}\n".format(
    row[time_col], row[tem_col], row[densidad_col], separator), data["data"]["rows"]))
s.save_file(file_txt_formatted, file_format)
# Crear un programa que recupere los datos del archivo anterior y los guarde en la colección experimentos_recuperados.


def save_to_mongo(file_to_read):
    list_to_save = []
    try:
        file_content = s.load_file(file_to_read)
        client = None
        try:
            # convert from text
            patternTIME = r".*(" + time_col + "):+\s*(?P<" + \
                time_col + ">[0-9]+)\s*?MIN[\s\n]*?"
            patternTEMP = r".*?(" + tem_col + ").*?(?P<" + \
                tem_col + ">[0-9]+)\s*?C[\s\n]+?"
            patternDENS = r".*?(" + densidad_col + \
                ").*?(?P<" + densidad_col + ">[0-9]+)\s*?U[\s\n]*?"
            for line in range(0, len(file_content), 4):
                # re.match(patternTIME + patternTEMP + patternDENS, "".join(file_content[line:line + 3])).groupdict()
                list_to_save.append(re.match(
                    patternTIME + patternTEMP + patternDENS, "".join(file_content[line:line + 3])).groupdict())
            client = MongoClient()

            db = client.test
            experimentos_recuperados = db.experimentos_recuperados

            ids = experimentos_recuperados.insert_many(list_to_save, True, False)
            print(ids.inserted_ids)
        except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to server: %s" % e)
        except pymongo.errors.BulkWriteError as bwe:
            print(bwe.details)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        finally:
            client.close()
        return True
    except:  # expression as identifier:
        return False


result = save_to_mongo(file_txt_formatted)
print(result)
