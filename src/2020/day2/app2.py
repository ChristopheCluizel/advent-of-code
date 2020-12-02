if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_lines = f.readlines()

    nb_valid_passwords = 0
    for raw_line in raw_lines:
        splits = raw_line.split(":")
        raw_policies = splits[0]
        password = splits[1].strip()

        policies_splits = raw_policies.split(" ")
        policy_range = policies_splits[0]
        letter = policies_splits[1]
        first_index = int(policy_range.split("-")[0]) - 1
        second_index = int(policy_range.split("-")[1]) - 1

        if (
            password[first_index] == letter or password[second_index] == letter
        ) and password[first_index] != password[second_index]:
            nb_valid_passwords += 1

    print(nb_valid_passwords)
