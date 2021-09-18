# Este algoritmo devuelve un número determinado de palabras de un
# diccionario ordenadas por coincidencia con respecto a una palabra de referencia.
# Utiliza para ello programación dinámica.


def get_num_matches(candidate, word):
    grid = [[0 for i in range(len(candidate))] for j in range(len(word))]
    row = 0

    for word_char in word:
        col = 0

        for current_char in candidate:
            if current_char == word_char:
                grid[row][col] = grid[row - 1][col - 1] + 1
            else:
                grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])

            col = col + 1

        row = row + 1

    return grid[len(grid) - 1][len(grid[0]) - 1]


def compose_suggestions_response(matches_by_word):
    suggestions = []

    for i in range(len(matches_by_word)):
        suggestions.append(matches_by_word[i][0])

    return suggestions


def get_suggestions(dictionary, word, num_suggestions):
    matches_by_word = [['', -1] for i in range(min(len(dictionary), num_suggestions))]

    for candidate in dictionary:
        matches = get_num_matches(candidate, word)

        for i in range(len(matches_by_word)):
            # si se encuentra un mejor resultado, se mueven a la derecha los anteriores y se inserta en esa posición
            if matches > matches_by_word[i][1]:
                for j in range(i, len(matches_by_word) - 1):
                    matches_by_word[j + 1] = matches_by_word[j]

                matches_by_word[i] = [candidate, matches]
                break

    return compose_suggestions_response(matches_by_word)


dictionary = set(['shed', 'mail', 'solve', 'crouch', 'fate'])
word = 'shedmavefate'

found = False

for current in dictionary:
    if current == word:
        found = True
        print(word + ' found in our dictionary')

if not found:
    print(word + ' not found, maybe you mean one of this: ' + ', '.join(get_suggestions(dictionary, word, 2)))
