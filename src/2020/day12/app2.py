import math


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"


class Ship:
    def __init__(self, position, waypoint):
        self.position = position
        self.waypoint = waypoint

    def __repr__(self):
        return f"position: {self.position}, waypoint: {self.waypoint}"

    def move(self, instruction):
        value = instruction["value"]
        waypoint = self.waypoint
        current_position = self.position
        x1 = current_position.x
        y1 = current_position.y
        x2 = waypoint.position.x
        y2 = waypoint.position.y

        new_position = Position(x1 + value * x2, y1 + value * y2)

        self.position = new_position


class Waypoint:
    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return f"position: {self.position}"

    def radian_to_degree(self, radian):
        return radian * 360 / (2 * math.pi)

    def degree_to_radian(self, degree):
        return degree * 2 * math.pi / 360

    def get_radius(self):
        x = self.position.x
        y = self.position.y

        return math.sqrt(x * x + y * y)

    def get_angle(self):
        x = self.position.x
        y = self.position.y

        if x > 0 and y >= 0:
            return math.atan(y / x)
        elif x > 0 and y < 0:
            return math.atan(y / x) + 2 * math.pi
        elif x < 0:
            return math.atan(y / x) + math.pi
        elif x == 0 and y > 0:
            return math.pi / 2
        elif x == 0 and y < 0:
            return 3 * math.pi / 2
        else:
            print("Get angle error")

    def move(self, instruction):
        action = instruction["action"]
        value = instruction["value"]
        current_x = self.position.x
        current_y = self.position.y

        if action == "N":
            self.position = Position(current_x, current_y + value)
        elif action == "S":
            self.position = Position(current_x, current_y - value)
        elif action == "E":
            self.position = Position(current_x + value, current_y)
        elif action == "W":
            self.position = Position(current_x - value, current_y)
        else:
            print("Move action is not valid.")

    def turn(self, instruction):
        action = instruction["action"]
        value = instruction["value"]
        current_angle = self.get_angle()
        r = self.get_radius()

        if action == "L":
            new_angle = self.radian_to_degree(current_angle) + value
        elif action == "R":
            new_angle = self.radian_to_degree(current_angle) - value
        else:
            print("Turn action is not valid.")

        new_angle = self.degree_to_radian(new_angle)
        self.position = Position(
            round(r * math.cos(new_angle)), round(r * math.sin(new_angle))
        )


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

    waypoint = Waypoint(Position(10, 1))
    ship = Ship(Position(0, 0), waypoint)

    print(f"initial ship: {ship}")

    for instruction in instructions:
        action = instruction["action"]

        if action in ["N", "S", "E", "W"]:
            waypoint.move(instruction)
        elif action in ["L", "R"]:
            waypoint.turn(instruction)
        elif action == "F":
            ship.move(instruction)
        else:
            print("Action is not valid.")

    print(f"final ship: {ship}")
    print(abs(ship.position.x) + abs(ship.position.y))
