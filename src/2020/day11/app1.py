import copy


def print_layout(layout):
    for j in range(0, len(layout)):
        line = ""
        for i in range(0, len(layout[0])):
            line += layout[j][i]
        print(line)


def load_layout():
    with open("./input.txt", "r") as f:
        lines = f.read().splitlines()

    res = []
    for j in range(0, len(lines)):
        res.append([])
        for letter in lines[j]:
            res[j].append(letter)

    return res


def get_nb_occupied_seats(layout, j, i):
    height = len(layout)
    width = len(layout[0])
    all_positions = []

    for item1 in [-1, 0, 1]:
        for item2 in [-1, 0, 1]:
            if (
                0 <= j + item1 < height
                and 0 <= i + item2 < width
                and not (item1 == 0 and item2 == 0)
            ):
                all_positions.append((j + item1, i + item2))

    counter = 0
    for position in all_positions:
        j = position[0]
        i = position[1]

        if layout[j][i] == "#":
            counter += 1

    return counter


def get_new_seat_state(layout, j, i):
    letter = layout[j][i]
    nb_occupied_seats = get_nb_occupied_seats(layout, j, i)

    if letter == ".":
        return "."
    elif letter == "L" and nb_occupied_seats == 0:
        return "#"
    elif letter == "#" and nb_occupied_seats >= 4:
        return "L"
    else:
        return letter


def get_next_state(layout):
    height = len(layout)
    width = len(layout[0])
    new_layout = copy.deepcopy(layout)

    for j in range(0, height):
        for i in range(0, width):
            new_seat_state = get_new_seat_state(layout, j, i)
            new_layout[j][i] = new_seat_state

    return new_layout


def are_same_layouts(layout1, layout2):
    height = len(layout1)
    width = len(layout1[0])

    for j in range(0, height):
        for i in range(0, width):
            if layout1[j][i] != layout2[j][i]:
                return False

    return True


if __name__ == "__main__":
    layout = load_layout()

    while True:
        next_layout = get_next_state(layout)

        if are_same_layouts(layout, next_layout):
            break

        layout = copy.deepcopy(next_layout)

    counter = 0
    height = len(next_layout)
    width = len(next_layout[0])
    for j in range(0, height):
        for i in range(0, width):
            if next_layout[j][i] == "#":
                counter += 1

    print(counter)
