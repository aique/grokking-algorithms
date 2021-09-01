# Algoritmo que determina el tamaño de una colección


def array_len(elements):
    if len(elements) == 0:
        return 0

    return 1 + array_len(elements[1:])


print(array_len([1, 2, 3]))
print(array_len([1, 2, 3, 4, 5]))
print(array_len([1, 2, 3, 4, 5, 6, 7]))
