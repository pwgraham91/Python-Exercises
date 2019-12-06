def solve():
    with open("./input.txt") as steps_text:
        first_line = steps_text.readline().split(",")
        first_line[-1] = first_line[-1][:-1]
        second_line = steps_text.readline().split(",")
        second_line[-1] = second_line[-1][:-1]

        first_line_spots, first_plain_spots = draw_line(first_line)
        second_line_spots, second_plain_spots = draw_line(second_line)

        intersection = first_line_spots.intersection(second_line_spots)
        return min([get_manhattan_distance(coordinates) for coordinates in intersection])


def get_manhattan_distance(coordinates):
    x, y = coordinates.split(",")
    return abs(int(x)) + abs(int(y))


def add_list_to_set(_list, _set, plain_list):
    hashed = ",".join([str(x) for x in _list])
    _set.add(hashed)
    plain_list.append(hashed)


def draw_line(instructions):
    list_line_spots = []
    line_spots = set()
    current_spot = [0, 0]
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        last_spot = current_spot
        for i in range(distance):
            modified_distance = i + 1
            if direction == "U":
                last_spot = [current_spot[0], current_spot[1] + modified_distance]
                add_list_to_set(last_spot, line_spots, list_line_spots)
            elif direction == "D":
                last_spot = [current_spot[0], current_spot[1] - modified_distance]
                add_list_to_set(last_spot, line_spots, list_line_spots)
            elif direction == "L":
                last_spot = [current_spot[0] - modified_distance, current_spot[1]]
                add_list_to_set(last_spot, line_spots, list_line_spots)
            else:
                last_spot = [current_spot[0] + modified_distance, current_spot[1]]
                add_list_to_set(last_spot, line_spots, list_line_spots)

        current_spot = last_spot

    return line_spots, list_line_spots


print(solve())


def solve_for_shortest_distance_to_collision():
    with open("./input.txt") as steps_text:
        first_line = steps_text.readline().split(",")
        first_line[-1] = first_line[-1][:-1]
        second_line = steps_text.readline().split(",")
        second_line[-1] = second_line[-1][:-1]

        first_line_spots, first_plain_spots, first_hashed_spot_counter = draw_line_2(first_line)
        second_line_spots, second_plain_spots, second_hashed_spot_counter = draw_line_2(second_line)

        intersections = first_line_spots.intersection(second_line_spots)
        min_steps = None
        for intersection in intersections:
            first_line_steps = first_hashed_spot_counter[intersection]
            second_line_steps = second_hashed_spot_counter[intersection]
            total_steps = first_line_steps + second_line_steps
            if min_steps is None or total_steps < min_steps:
                min_steps = total_steps
        return min_steps


def add_list_to_set_2(_list, _set, plain_list, step_counter, num_steps):
    hashed = ",".join([str(x) for x in _list])
    _set.add(hashed)
    plain_list.append(hashed)
    if not step_counter.get(hashed):
        step_counter[hashed] = num_steps


def draw_line_2(instructions):
    hashed_spot_step_counter = dict()
    list_line_spots = []
    line_spots = set()
    current_spot = [0, 0]
    counter = 0
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        last_spot = current_spot
        for i in range(distance):
            counter += 1
            modified_distance = i + 1
            if direction == "U":
                last_spot = [current_spot[0], current_spot[1] + modified_distance]
                add_list_to_set_2(last_spot, line_spots, list_line_spots, hashed_spot_step_counter, counter)
            elif direction == "D":
                last_spot = [current_spot[0], current_spot[1] - modified_distance]
                add_list_to_set_2(last_spot, line_spots, list_line_spots, hashed_spot_step_counter, counter)
            elif direction == "L":
                last_spot = [current_spot[0] - modified_distance, current_spot[1]]
                add_list_to_set_2(last_spot, line_spots, list_line_spots, hashed_spot_step_counter, counter)
            else:
                last_spot = [current_spot[0] + modified_distance, current_spot[1]]
                add_list_to_set_2(last_spot, line_spots, list_line_spots, hashed_spot_step_counter, counter)

        current_spot = last_spot

    return line_spots, list_line_spots, hashed_spot_step_counter


print(solve_for_shortest_distance_to_collision())

