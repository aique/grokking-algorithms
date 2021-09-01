# Algoritmo que calcula el factorial de un número


def factorial(x):
    if x == 1:
        return 1  # caso base
    else:
        return x * factorial(x - 1)  # caso recursivo


print(factorial(5))
