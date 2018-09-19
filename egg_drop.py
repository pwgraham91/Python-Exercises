"""
A building has 100 floors. One of the floors is the highest floor an egg can be dropped from without breaking.

If an egg is dropped from above that floor, it will break. If it is dropped from that floor or below, it will be
completely undamaged and you can drop the egg again.

Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.
"""
import random


def reckless_check_floor(state):
    check_floor = int((state['floor_max'] + state['floor_min']) / 2)
    if check_floor in state['checked_floors']:
        check_floor += 1
    print(check_floor)

    state['checked_floors'].append(check_floor)
    if check_floor > state['breaking_floor']:
        state['floor_max'] = check_floor
        return
    else:
        state['floor_min'] = check_floor
        reckless_check_floor(state)


def careful_check_floor(state):
    state['num_drops'] += 1

    check_floor = state['floor_min'] + 1
    print(check_floor)

    state['checked_floors'].append(check_floor)
    if check_floor > state['breaking_floor']:
        return state
    else:
        state['floor_min'] = check_floor
        return careful_check_floor(state)


def find_max_floor(num_floors, breaking_floor):
    state = {
        'num_drops': 0,
        'floor_min': 1,
        'floor_max': num_floors,
        'breaking_floor': breaking_floor,
        'checked_floors': [1]
    }

    reckless_check_floor(state)
    return careful_check_floor(state)


floor = random.randrange(0, 100)

state = find_max_floor(100, floor)
print(state)
print(len(state['checked_floors']))
