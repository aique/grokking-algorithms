# Búsqueda del camino más óptimo en un grafo con pesos, utilizando el algoritmo de Dijksta.


def search():
    graph = set_up_graph()
    costs = set_up_costs()
    parents = set_up_parents()
    processed = []

    node = find_lowest_cost_node(costs, processed)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    print('lowest cost: ',  cost)
    print('lowest cost path: ', get_lowest_path('start', 'end', parents))


def get_lowest_path(from_node, to_node, parents):
    path = [to_node]
    parent = parents[to_node]

    while parent is not from_node:
        path.insert(0, parent)
        parent = parents[parent]

    path.insert(0, from_node)

    return path


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def set_up_graph():
    graph = {}

    graph['start'] = {}
    graph['a'] = {}
    graph['b'] = {}
    graph['end'] = {}

    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a']['end'] = 1
    graph['b']['a'] = 3
    graph['b']['end'] = 5

    return graph


def set_up_costs():
    costs = {}

    costs['a'] = 6
    costs['b'] = 2
    costs['end'] = float('inf')

    return costs


def set_up_parents():
    parents = {}

    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['end'] = None

    return parents


search()
