# Este algoritmo devuelve un número determinado de palabras de un
# diccionario ordenadas por coincidencia con respecto a una palabra de referencia.
# Utiliza para ello programación dinámica.

def get_suggestions(dictionary, word, num_sugestions):
    matches = {}

    for dictionary_word in dictionary:
        grid = [[0 for i in range(len(dictionary_word))] for j in range(len(word))]
        row = 0

        for current_char in word:
            col = 0

            for dictionary_char in dictionary_word:
                if dictionary_char == current_char:
                    grid[row][col] = grid[row - 1][col - 1] + 1
                else:
                    grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])

                col = col + 1

            row = row + 1

        matches[dictionary_word] = grid[len(grid) - 1][len(grid[0]) - 1]

    return {k: v for k, v in sorted(matches.items(), key=lambda item: item[1], reverse=True)[:num_sugestions]}


dictionary = set(['shed', 'mail', 'solve', 'crouch', 'fate'])
word = 'soteouch'

found = False

for current in dictionary:
    if current == word:
        found = True
        print(word + ' found in our dictionary')

if not found:
    print(word + ' not found, maybe you mean one of this: ' + ', '.join(get_suggestions(dictionary, word, 2)))
