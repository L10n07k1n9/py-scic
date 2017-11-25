# Crea un programa que defina la funcion 'multiplos (m,n)' que devuelve una lista con los primeros  n multiplos del numero m comenzando en 1.
# Ejemplo:
# multiplos(3,5)->[1,3,6,9,12]


def multiplos(m, n):
    return [1] + list(map(lambda x: x * m, range(1, n)))
    # for i in range(1, n):
    #     p = i * m
    #     result.append(p)
# Crea un programa que defina la funcion 'criba' que ajusta a 0 todos los multplos de m, comenzando en el indice m
# Ejemplo
# A=[1,3,4,5,6,7,8,9,10,11,12]
# criba(3,A)->A=[1,2,0,4,5,0,7,8,0,9,0]


def criba(m, numbers):
    TACHE = 0
    for i in range(0, len(numbers)):
        if (i + 1) % m == 0:
            numbers[i] = TACHE
    return numbers
    # result, ix = [], 1

    # for n in numbers:
    #     if ix % m == 0:
    #         result.append(0)
    #     else:
    #         result.append(n)
    #     ix = ix + 1
    # return result
