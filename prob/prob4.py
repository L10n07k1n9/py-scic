import random
# Crear un diccionario que almacene los valores de un producto (nombre, marca, descripción, costo, etc).
product={
    "name":"Fabuloso","brand":"x","descr":"shceisse","cost":122.12
    }
product["bar_code"]="awd112312"
# Crear un diccionario que almacene los datos de un experimento (nombre, tiempo, PH, temperatura, etc).
sample={
    "name":"water in cdmx",
    "time":"21/08/2017",
    "PH":4.2,
    # Celsius degrees
    "temp":"20"
}
# Generar una lista de diccionarios con 1000 puntos aleatorios en el intervalor (-10, 10) en ambos ejes.
dList=[]
for i in range(0,100+1):
    pointX,pointY=random.randint(-10  , 10)  ,random.randint(-10  , 10)
    dList.append({"x":pointX,"y":pointY})
# print(dList)
# De la lista de puntos anterior, filtrar los puntos que se ubican a máximo 2 unidades del punto (1, 2).
filtered_2units=[]
filtered_2units=list(filter(lambda el:((1-el["x"])**2 + (2-el["y"])**2)**0.5<=2,dList))
print("# De la lista de puntos anterior, filtrar los puntos que se ubican a máximo 2 unidades del punto (1, 2).")
print(filtered_2units)
# De la lista de puntos anterior, filtrar los puntos que tienen un X negativo.
filtered_X_neg=list(filter(lambda el:el["x"]<0,dList))
print("De la lista de puntos anterior, filtrar los puntos que tienen un X negativo")
print(filtered_X_neg)
# De la lista anterior, generar otra lista donde se intercambien los valores de las X y las Y.
xchange=[]
for i in filtered_X_neg:
    xchange.append({"x":i["y"],"y": i["x"]})
print(" De la lista anterior, generar otra lista donde se intercambien los valores de las X y las Y")
print(xchange)