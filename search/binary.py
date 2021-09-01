# Búsqueda binaria de un elemento en una colección


def binary_search(collection, item):
    low = 0
    high = len(collection) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = collection[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 7))
print(binary_search(my_list, -1))
