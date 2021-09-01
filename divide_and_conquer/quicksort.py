from random import randrange

# Ordenación de elementos en una colección con complejidad O(n*log n).


def quicksort(elements):
    if len(elements) < 2:
        return elements

    pivot = elements.pop(randrange(len(elements)))
    smallers = [i for i in elements if i <= pivot]
    greaters = [i for i in elements if i > pivot]

    return quicksort(smallers) + [pivot] + quicksort(greaters)


print(quicksort([33, 10, 15, 7]))
