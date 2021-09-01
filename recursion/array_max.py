# Algoritmo que determina el número mayor de una colección


def array_max(elements):
    if len(elements) == 1:
        return elements[0]
    if len(elements) == 2:
        return max_num(elements[0], elements[1])

    return max_num(elements[0], array_max(elements[1:]))


def max_num(element1, element2):
    if element1 > element2:
        return element1
    else:
        return element2


print(array_max([3]))
print(array_max([3, 7]))
print(array_max([3, 7, 2, 8, 4, 9, 3]))
