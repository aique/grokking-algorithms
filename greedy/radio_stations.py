# Solución para la obtención del mínimo número de emisoras de radio
# que cubren un número determinado de estados utilizando un algoritmo devorador.


def get_best_station(states_needed):
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station

        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    return best_station


def get_station_list(stations, states_needed):
    station_list = set()

    while states_needed:
        best_station = get_best_station(states_needed)

        if best_station is None:
            return station_list

        station_list.add(best_station)
        states_needed -= stations[best_station]

    return station_list


stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

print(get_station_list(
    stations,
    set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
))
