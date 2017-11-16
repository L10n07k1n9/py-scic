import math
import matplotlib.pyplot as plt
# Generar 11 valores equidistantes en el intervalo de [a, b]. Por ejemplo, si a = 1 y b = 3 el resultado sería [1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3].
div,a,b,X=10,1,100,[]
def Generator1(a,b):
    l=[]
    for i in range(div):
        diff=b-a
        x=(diff)/div
        l.append(x*i)
    return l
X=Generator1(a,b)
print (X)
# Generar una lista Y que aplique la función sen(x) para cada x en la lista anterior.
def Generator2(X):
    # sine in rad
    return list(map(lambda x:math.sin(x),X)) 
Y=Generator2(X)
print (Y)
# Graficar X y Y para las listas anteriores en color rojo punteado r--.
plt.plot(X,Y,"r--")