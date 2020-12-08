def load_instructions():
    with open("./input.txt", "r") as f:
        return f.read().splitlines()


def format_instructions(raw_instructions):
    res = []

    for raw_instruction in raw_instructions:

        splits = raw_instruction.split(" ")
        operation = splits[0]
        argument = int(splits[1])

        temp = {
            "operation": operation,
            "argument": argument,
            "used": False,
        }
        res.append(temp)

    return res


def execute_instruction(instruction, current_index, accumulator):
    operation = instruction["operation"]
    argument = instruction["argument"]
    next_index = current_index

    if instruction["used"]:
        return None, True, accumulator
    else:
        instruction["used"] = True
        if operation == "acc":
            accumulator += argument
            next_index += 1
        elif operation == "jmp":
            next_index += argument
        else:
            next_index += 1

        return next_index, False, accumulator


if __name__ == "__main__":
    raw_instructions = load_instructions()
    instructions = format_instructions(raw_instructions)

    accumulator = 0
    current_index = 0
    repeat = False

    while not repeat:
        instruction = instructions[current_index]
        current_index, repeat, accumulator = execute_instruction(
            instruction, current_index, accumulator
        )

    print(accumulator)
