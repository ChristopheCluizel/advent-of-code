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


def see_occupied_seat(layout, j, i, direction_j, direction_i):
    height = len(layout)
    width = len(layout[0])

    while True:
        j = j + direction_j
        i = i + direction_i

        if (j < 0 or height <= j) or (i < 0 or width <= i) or layout[j][i] == "L":
            break

        if layout[j][i] == "#":
            return True

    return False


def get_nb_occupied_seats(layout, j, i):
    counter = 0
    for direction_j in [-1, 0, 1]:
        for direction_i in [-1, 0, 1]:
            if not (direction_j == 0 and direction_i == 0):
                if see_occupied_seat(layout, j, i, direction_j, direction_i):
                    counter += 1

    return counter


def get_new_seat_state(layout, j, i):
    letter = layout[j][i]

    if letter == ".":
        return "."

    nb_occupied_seats = get_nb_occupied_seats(layout, j, i)

    if letter == "L" and nb_occupied_seats == 0:
        return "#"
    elif letter == "#" and nb_occupied_seats >= 5:
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
