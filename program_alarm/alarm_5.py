""" https://adventofcode.com/2019/day/5 """


class StepTracker:
    steps = None
    current_step_index = 0

    def __init__(self, steps):
        self.steps = steps

    def get_opcode_and_instructions(self):
        current_step = str(self.steps[self.current_step_index]).zfill(5)
        self.current_step_index += 1
        opcode = int(current_step[-2:])
        instructions = [x for x in current_step[:3]]
        return opcode, instructions

    def get_next_value(self, instructions):
        instruction = int(instructions.pop())
        if instruction == 0:
            value = self.steps[self.steps[self.current_step_index]]
        else:
            value = self.steps[self.current_step_index]

        self.current_step_index += 1

        return value

    def set_value(self, instructions, value):
        instruction = int(instructions.pop())
        if instruction == 0:
            self.steps[self.steps[self.current_step_index]] = value
        else:
            self.steps[self.current_step_index] = value
        self.current_step_index += 1


def solve():
    with open("./input_5.txt") as steps_text:
        steps_text_string = steps_text.readline()
        # steps_text_string = "1002,4,3,4,33"
        step_tracker = StepTracker([int(x) for x in steps_text_string.split(",")])

        while True:
            opcode, instructions = step_tracker.get_opcode_and_instructions()

            if opcode == 1:
                first_value = step_tracker.get_next_value(instructions)
                second_value = step_tracker.get_next_value(instructions)
                value = first_value + second_value

                step_tracker.set_value(instructions, value)
            elif opcode == 2:
                first_value = step_tracker.get_next_value(instructions)
                second_value = step_tracker.get_next_value(instructions)
                value = first_value * second_value

                step_tracker.set_value(instructions, value)
            elif opcode == 3:
                value = 1
                step_tracker.set_value(instructions, value)
            elif opcode == 4:
                first_value = step_tracker.get_next_value(instructions)
                print("opcode 4 {}".format(first_value))
            elif opcode == 99:
                return step_tracker.steps[0]


print(solve())
