import math
from functools import reduce


def build_level(raw_lines, ratio):
    nb_lines = len(raw_lines)
    nb_columns = len(raw_lines[0])

    level = []
    for index, raw_line in enumerate(raw_lines):
        raw_line = raw_line * math.ceil(ratio * nb_lines / nb_columns)
        level.append([])
        for character in raw_line:
            level[index].append(character)

    return level


def get_trees_number(level, move):
    current_position = (0, 0)
    nb_trees = 0
    while current_position[0] < nb_lines:
        x, y = current_position[0], current_position[1]
        if level[x][y] == "#":
            nb_trees += 1

        current_position = (x + move[1], y + move[0])

    return nb_trees


if __name__ == "__main__":
    with open("input.txt") as f:
        raw_lines = f.read().splitlines()

    ratios = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    all_trees = []
    for ratio in ratios:
        level = build_level(raw_lines, ratio[0] / ratio[1])
        nb_lines = len(level)

        nb_trees = get_trees_number(level, (ratio[0], ratio[1]))
        all_trees.append(nb_trees)

    res = reduce(lambda x1, x2: x1 * x2, all_trees)
    print(all_trees)
    print(res)
