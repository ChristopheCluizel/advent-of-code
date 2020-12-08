import copy


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
        return next_index, True, accumulator
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


def exectute_instructions(instructions):
    accumulator = 0
    current_index = 0
    repeat = False

    while not repeat and current_index < len(instructions):
        instruction = instructions[current_index]
        current_index, repeat, accumulator = execute_instruction(
            instruction, current_index, accumulator
        )

    return current_index == len(instructions), accumulator


def generate_modified_instructions(original_instructions):
    all_instructions = [original_instructions]

    for index, instruction in enumerate(original_instructions):
        operation = instruction["operation"]

        if operation in ["jmp", "nop"]:
            new_instructions = copy.deepcopy(original_instructions)

            if operation == "jmp":
                new_instructions[index]["operation"] = "nop"
            else:
                new_instructions[index]["operation"] = "jmp"
            all_instructions.append(new_instructions)

    return all_instructions


if __name__ == "__main__":
    raw_instructions = load_instructions()
    instructions = format_instructions(raw_instructions)

    modified_instructions = generate_modified_instructions(instructions)

    for modified_instruction in modified_instructions:
        normal_exit, accumulator = exectute_instructions(modified_instruction)

        if normal_exit:
            print(accumulator)
            break
