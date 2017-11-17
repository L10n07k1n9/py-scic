# Crea un programa que genere los primero 20 números definidos por la sucesión f(0) = 0, f(1) = 4, f(2) = 3 y f(n) = 2 * f(n - 2) - f(n - 1) + f(n - 3) para n >= 3
BASE_CASES = {0: 0, 1: 4, 2: 3}


def f(n):
    if n <= 0:
        return BASE_CASES[0]
    elif n <= 2:
        return BASE_CASES[n]
    else:
        # f(n) = 2 * f(n - 2) - f(n - 1) + f(n - 3) para n >= 3
        return 2 * f(n - 2) - f(n - 1) + f(n - 3)


def GeneratorSucesionChistosa(x):
    r = []
    for i in range(0, x + 1):
        r.append(f(i))
    return r


r1 = GeneratorSucesionChistosa(20)
print(r1)

# Crea un filtro para la sucesión anterior que almacene todos los números que son multiplos de 7 (x módulo 7 congruente con 0).


def GeneratorSucesionChistosa_Mod7(x):
    r, a, b, m = [], 0, 0, 7
    for n in range(0, x + 1):
        b = f(n)
        a = b % m
        if a == 0:
            r.append(b)
    return r


r2 = GeneratorSucesionChistosa_Mod7(20)
print(r2)
