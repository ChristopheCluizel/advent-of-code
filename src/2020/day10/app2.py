def load_data():
    with open("./input.txt", "r") as f:
        return [int(item) for item in f.read().splitlines()]


def get_possible_joltages(start_index):
    res = []
    end_index = start_index + 1

    while True:
        if end_index >= len(numbers):
            break

        diff = abs(numbers[start_index] - numbers[end_index])

        if diff > 3:
            break

        res.append(numbers[end_index])
        end_index += 1

    return res


def count_arrangements(numbers, possible_joltages):
    def get_number_leafs(value, leafs_dict):
        children_values = possible_joltages[value]

        if len(children_values) == 0:
            return 1

        if value in leafs_dict.keys():
            return leafs_dict[value]

        res = 0
        for child_value in children_values:
            res += get_number_leafs(child_value, leafs_dict)

        leafs_dict[value] = res

        return res

    counter = get_number_leafs(0, {})

    return counter


if __name__ == "__main__":
    numbers = load_data()

    device_builtin_joltage = max(numbers) + 3
    numbers.append(0)
    numbers.append(device_builtin_joltage)
    numbers = sorted(numbers)

    possible_joltages = {}
    for index, value in enumerate(numbers):
        values = get_possible_joltages(index)
        possible_joltages[value] = values

    arrangements_count = count_arrangements(numbers, possible_joltages)

    print(arrangements_count)
