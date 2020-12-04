import re


def load_data(filepath):
    with open(filepath) as f:
        return f.read()


def load_passports(raw_string):
    passports = []
    formatted_string = raw_string.replace("\n\n", "|").replace("\n", " ")
    passports = formatted_string.split("|")

    return passports


def validate_string_integer(string_integer, min, max):
    try:
        value = int(string_integer)
        if value < min or value > max:
            return False
    except Exception:
        return False

    return True


def is_valid_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    pairs = passport.split(" ")
    keys = [pair.split(":")[0] for pair in pairs]

    for required_field in required_fields:
        if required_field not in keys:
            return False

    for pair in pairs:
        splits = pair.split(":")
        key = splits[0]
        value = splits[1]

        if key == "byr":
            if not validate_string_integer(value, 1920, 2002):
                return False
        elif key == "iyr":
            if not validate_string_integer(value, 2010, 2020):
                return False
        elif key == "eyr":
            if not validate_string_integer(value, 2020, 2030):
                return False
        elif key == "hgt":
            if "cm" in value:
                number = value.split("cm")[0]
                if not validate_string_integer(number, 150, 193):
                    return False
            elif "in" in value:
                number = value.split("in")[0]
                if not validate_string_integer(number, 59, 76):
                    return False
            else:
                return False
        elif key == "hcl":
            regex = re.compile("^#[0-9a-f]{6}$")
            match = bool(regex.match(value))

            if not match:
                return False
        elif key == "ecl":
            enum = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if value not in enum:
                return False
        elif key == "pid":
            regex = re.compile("^[0-9]{9}$")
            match = bool(regex.match(value))

            if not match:
                return False
        elif key == "cid":
            pass
        else:
            return False

    return True


if __name__ == "__main__":
    raw_string = load_data("./resources/input.txt")
    passports = load_passports(raw_string)

    valid_passports_count = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports_count += 1

    print(valid_passports_count)
