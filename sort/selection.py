# Ordenación de elementos de una colección buscando el siguiente menor
# y colocándolo al principio de la colección. Complejidad cuadrática O(n²).


def selection_sort(collection):
    sort_collection = []

    for i in range(len(collection)):
        smallest = smallest_index(collection)
        sort_collection.append(collection.pop(smallest))

    return sort_collection


def smallest_index(collection):
    index = 0
    smallest = collection[index]

    for i in range(1, len(collection)):
        if collection[i] < smallest:
            smallest = collection[i]
            index = i

    return index


print(selection_sort([5, 3, 7, 1, 15]))
