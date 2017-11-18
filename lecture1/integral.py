import math


def f(x):
    return x**2 - 2 * x + 4


def test_raise():
    raise ValueError("'a' must not be greater or equal to 'b'!")


def Integral():
    # limits where a < b
    a, b = 0, 3
    # number of points to evvaluate
    n, integralAprox = 5, 0
    # delta for diff of point in n
    delta = (b - a) / n
    for i in range(0, n):
        # get the base
        xMin = a + i * delta
        xMax = a + (i + 1) * delta

        # get the height from the base point of the f(x)
        hMin = f(xMin)
        hMax = f(xMax)

        height = (hMin + hMax) / 2
        base = xMax - xMin

        area = base * height

        integralAprox += area
    return integralAprox


print("Integral of f(x)={:.4f}".format(Integral()))
