import math


def get_position(boarding_pass):
    row = (0, 127)
    column = (0, 7)

    for letter in boarding_pass:
        row_middle = (row[0] + row[1]) / 2
        column_middle = (column[0] + column[1]) / 2

        if letter == "F":
            row = (row[0], math.floor(row_middle))
        elif letter == "B":
            row = (math.ceil(row_middle), row[1])
        elif letter == "L":
            column = (column[0], math.floor(column_middle))
        else:
            column = (math.ceil(column_middle), column[1])

    return row[0], column[0]


def get_id(boarding_pass):
    row, column = get_position(boarding_pass)
    id = row * 8 + column

    return id


if __name__ == "__main__":
    assert get_id("FBFBBFFRLR") == 357
    assert get_id("BFFFBBFRRR") == 567
    assert get_id("FFFBBBFRRR") == 119
    assert get_id("BBFFBBFRLL") == 820

    with open("./input.txt", "r") as f:
        boarding_passes = f.read().splitlines()

    ids = []
    for boarding_pass in boarding_passes:
        id = get_id(boarding_pass)
        ids.append(id)

    max_id = max(ids)

    my_id = None
    for id in range(0, max_id + 1):
        if id not in ids:
            missing_id = id
            if missing_id - 1 in ids and missing_id + 1 in ids:
                my_id = id

    print(my_id)
