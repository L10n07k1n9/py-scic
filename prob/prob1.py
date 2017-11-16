# Crea un programa que genere los primero 20 números definidos por la sucesión f(0) = 0, f(1) = 4, f(2) = 3 y f(n) = 2 * f(n - 2) - f(n - 1) + f(n - 3) para n >= 3
def BaseCases(x):
    return {0:0,1:4,2:3}[x]
def Generator20FirstNum:
    
# Crea un filtro para la sucesión anterior que almacene todos los números que son multiplos de 7 (x módulo 7 congruente con 0).