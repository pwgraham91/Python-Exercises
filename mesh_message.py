# https://www.interviewcake.com/question/python/mesh-message

network = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam': ['Nathan', 'Jayden', 'William'],
    'Omar': ['Ren', 'Min', 'Scott'],
    'Nathan': ['Noam', 'Miguel'],
    'Scott': ['Omar'],
    'Sofia': ['Adam'],
    'Lucas': ['Adam'],
    'Liam': ['Miguel'],
}


def route_iteratively(originator, receiver):
    if originator == receiver:
        return [originator]

    seen_carriers = {originator}

    check_routes = [[originator]]

    while check_routes:
        current_route = check_routes.pop(0)
        current_phone = current_route[-1]

        for phone in network[current_phone]:
            if receiver == phone:
                current_route.append(receiver)
                return current_route

            if phone not in seen_carriers:
                new_route = current_route[:]
                new_route.append(phone)
                seen_carriers.add(phone)
                check_routes.append(new_route)


assert route_iteratively('Jayden', 'Adam') == ['Jayden', 'Amelia', 'Adam']
assert route_iteratively('Jayden', 'No One') is None
assert route_iteratively('Jayden', 'Jayden') == ['Jayden']
assert route_iteratively('Adam', 'William') == ['Adam', 'Amelia', 'Jayden', 'Min', 'William']
assert route_iteratively('Miguel', 'Jayden') == ['Miguel', 'Amelia', 'Jayden']

