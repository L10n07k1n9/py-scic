import math
# Problemas

# Crea una función llamada Integral(f, a, b, n) que reciba los parámetros f - función, a - número, b - número y n - número.

# Dentro de la función Integral calcula la integral aproximada con los parámetros enviados y devuelve el dicho valor.

# Ejecuta el siguiente código poniendo antes la definición de la función Integral y corrobora que el resultado sea correcto:

# # TODO: Pon aqui la función Integral(f, a, b, n)


def func_def(x):
    return x**2 - 2 * x + 4


def integral(a, b, n, f=func_def):
    # limits where a (start point) < b (end point)
    # delta for diff of point in n
    delta, integralAprox = abs(b - a) / n, 0
    for i in range(0, n):
        # get the base
        xMin = a + i * delta
        xMax = a + (i + 1) * delta

        # get the height from the base point of the f(x)
        hMin = f(xMin)
        hMax = f(xMax)

        # we obtain the avg y1 and y2, its a fair simple aprox among this distances in term of height, it is a crecient function so there is no problem with using sum f:R->R
        height = (hMax + hMin) / 2
        base = xMax - xMin

        area = base * height

        integralAprox += area
    return integralAprox

# I = Integral(lambda x: x ** 2 - 2 * x + 4, 0, 3, 500)


# Comenta brevemente en tu código mediante un comentario en varias líneas (usando """) que significa lambda x: x ** 2 - 2 * x + 4 y que uso tiene en este código.
"""
Lambda expressions are used to map a function definition (inline) in form of a subexpression mapped to "n" variables
"""


# print("Integral de f(x)={:.4f}".format(I))
# a initial point to evaluate
# b end point to evaluate
a, b, n = 0, 3, 5000
print("Integral of f(x)={:.4f}".format(
    integral(a, b, n, lambda x: x**2 - 2 * x + 4)))
