def load_data():
    with open("./input.txt", "r") as f:
        return [int(item) for item in f.read().splitlines()]


def get_res(numbers, nb_preamble):
    current_index = nb_preamble

    for index in range(current_index, len(numbers)):
        preamble_numbers = numbers[index - nb_preamble : index]
        current_number = numbers[index]

        find = False
        for preamble_number in preamble_numbers:
            diff = current_number - preamble_number
            if diff in preamble_numbers and diff != preamble_number:
                find = True

        if not find:
            return current_number


if __name__ == "__main__":
    numbers = load_data()
    res = get_res(numbers, 25)

    print(res)
