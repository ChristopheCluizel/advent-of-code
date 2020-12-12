class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"


class Ship:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __repr__(self):
        return f"position: {self.position}, direction: {self.direction}"

    def direction_to_angle(self, direction):
        orientations = {"E": 0, "N": 90, "W": 180, "S": 270}

        return orientations[direction]

    def angle_to_direction(self, angle):
        orientations = {0: "E", 90: "N", 180: "W", 270: "S"}
        return orientations[angle]

    def move(self, instruction):
        action = instruction["action"]
        value = instruction["value"]
        current_x = self.position.x
        current_y = self.position.y

        if action == "F":
            action = self.direction

        if action == "N":
            self.position = Position(current_x, current_y - value)
        elif action == "S":
            self.position = Position(current_x, current_y + value)
        elif action == "E":
            self.position = Position(current_x + value, current_y)
        elif action == "W":
            self.position = Position(current_x - value, current_y)
        else:
            print("Move action is not valid.")

    def turn(self, instruction):
        action = instruction["action"]
        value = instruction["value"]
        angle = self.direction_to_angle(self.direction)

        if action == "L":
            angle = (angle + value) % 360
        elif action == "R":
            angle = (angle - value) % 360
        else:
            print("Turn action is not valid.")

        self.direction = self.angle_to_direction(angle)


def load_instructions():
    with open("./input.txt", "r") as f:
        return f.read().splitlines()


def format_instructions(raw_instructions):
    res = []

    for instruction in raw_instructions:
        action = instruction[0]
        value = "".join(instruction[1:])
        res.append({"action": action, "value": int(value)})

    return res


if __name__ == "__main__":
    raw_instructions = load_instructions()
    instructions = format_instructions(raw_instructions)

    ship = Ship(Position(0, 0), "E")

    for instruction in instructions:
        action = instruction["action"]

        if action in ["N", "S", "E", "W", "F"]:
            ship.move(instruction)
        elif action in ["L", "R"]:
            ship.turn(instruction)
        else:
            print("Action is not valid.")

    print(f"final ship: {ship}")
    print(abs(ship.position.x) + abs(ship.position.y))
