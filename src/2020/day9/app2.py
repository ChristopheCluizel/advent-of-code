def load_data():
    with open("./input.txt", "r") as f:
        return [int(item) for item in f.read().splitlines()]


def get_invalid_number(numbers, nb_preamble):
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


def find_sum_numbers(numbers, invalid_number):
    for index in range(0, len(numbers)):
        min_index = index
        max_index = min(index + 1, len(numbers))
        sub_numbers = numbers[min_index : max_index + 1]

        while sum(sub_numbers) < invalid_number and max_index < len(numbers):
            max_index += 1
            sub_numbers = numbers[min_index : max_index + 1]

            if sum(sub_numbers) == invalid_number:
                return sub_numbers

    return []


if __name__ == "__main__":
    numbers = load_data()
    invalid_number = get_invalid_number(numbers, 25)

    print(f"invalid number: {invalid_number}")

    sum_numbers = find_sum_numbers(numbers, invalid_number)

    print(min(sum_numbers) + max(sum_numbers))
