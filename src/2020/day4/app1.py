def load_data(filepath):
    with open(filepath) as f:
        return f.read()


def load_passports(raw_string):
    passports = []
    formatted_string = raw_string.replace("\n\n", "|").replace("\n", " ")
    passports = formatted_string.split("|")

    return passports


def is_valid_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    pairs = passport.split(" ")
    keys = [pair.split(":")[0] for pair in pairs]

    for required_field in required_fields:
        if required_field not in keys:
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
