from collections import deque

# Búsqueda en anchura sobre un grafo.


def breadth_first_sort(name, graph):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_what_i_look_for(person):
                print(person + ' is what I look for')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    print('No results found')

    return False


def is_what_i_look_for(name):
    return name == 'anuj'


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

breadth_first_sort('you', graph)
