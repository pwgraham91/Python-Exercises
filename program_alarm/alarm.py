def solve():
    with open("./input.txt") as steps_text:
        steps = [int(x) for x in steps_text.readline().split(",")]
        steps[1] = 12
        steps[2] = 2
        current_step_index = 0

        while True:
            current_step = steps[current_step_index]

            if current_step == 1:
                value = steps[steps[current_step_index + 1]] + steps[steps[current_step_index + 2]]
            elif current_step == 2:
                value = steps[steps[current_step_index + 1]] * steps[steps[current_step_index + 2]]
            elif current_step == 99:
                return steps[0]

            steps[steps[current_step_index + 3]] = value

            current_step_index += 4


def solve_for_value():
    with open("./input.txt") as steps_text:
        original_steps = [int(x) for x in steps_text.readline().split(",")]
        for a in range(100):
            for b in range(100):
                steps = original_steps.copy()
                steps[1] = a
                steps[2] = b

                current_step_index = 0

                while True:
                    current_step = steps[current_step_index]

                    if current_step == 1:
                        value = steps[steps[current_step_index + 1]] + steps[steps[current_step_index + 2]]
                    elif current_step == 2:
                        value = steps[steps[current_step_index + 1]] * steps[steps[current_step_index + 2]]
                    elif current_step == 99:
                        if value == 19690720:
                            return a, b
                        break

                    steps[steps[current_step_index + 3]] = value

                    current_step_index += 4

print(solve_for_value())
