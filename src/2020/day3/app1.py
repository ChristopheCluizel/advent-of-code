import math

if __name__ == "__main__":
    with open("input.txt") as f:
        raw_lines = f.read().splitlines()

    nb_lines = len(raw_lines)
    nb_columns = len(raw_lines[0])

    level = []
    for index, raw_line in enumerate(raw_lines):
        raw_line = raw_line * math.ceil((3 / 1) * nb_lines / nb_columns)
        level.append([])
        for character in raw_line:
            level[index].append(character)

    print(f"nb_lines: {len(level)}, nb_columns: {len(level[0])}")

    current_position = (0, 0)
    nb_trees = 0
    while current_position[0] < nb_lines:
        x, y = current_position[0], current_position[1]
        if level[x][y] == "#":
            nb_trees += 1

        current_position = (x + 1, y + 3)

    print(nb_trees)
