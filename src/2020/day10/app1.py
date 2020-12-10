from collections import Counter


def load_data():
    with open("./input.txt", "r") as f:
        return [int(item) for item in f.read().splitlines()]


def create_tuples(numbers):
    res = []

    for start_index in range(0, len(numbers) - 1):
        nb_1 = numbers[start_index]
        nb_2 = numbers[start_index + 1]

        res.append((nb_1, nb_2))

    return res


if __name__ == "__main__":
    numbers = load_data()

    device_builtin_joltage = max(numbers) + 3
    numbers.append(0)
    numbers.append(device_builtin_joltage)
    numbers = sorted(numbers)

    tuples = create_tuples(numbers)
    res = [t[1] - t[0] for t in tuples]

    counter = Counter(res)

    print(counter)
    print(counter[1] * counter[3])
