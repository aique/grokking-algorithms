# Algoritmo que determina el sumatorio de los componentes de una colección


def array_sum(elements):
    if len(elements) == 0:
        return 0

    return elements[0] + array_sum(elements[1:])


print(array_sum([3, 5, 1]))
