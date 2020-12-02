if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_lines = f.readlines()

    lines = []
    for raw_line in raw_lines:
        splits = raw_line.split(":")
        raw_policies = splits[0]
        password = splits[1].strip()

        policies_splits = raw_policies.split(" ")
        policy_range = policies_splits[0]
        letter = policies_splits[1]
        min_occurrence = int(policy_range.split("-")[0])
        max_occurrence = int(policy_range.split("-")[1])

        tuple = (password, letter, min_occurrence, max_occurrence)
        lines.append(tuple)

    nb_valid_passwords = 0
    for line in lines:
        password = line[0]
        letter = line[1]
        counter = 0
        for string_letter in password:
            if string_letter == letter:
                counter += 1

        if line[2] <= counter <= line[3]:
            nb_valid_passwords += 1

    print(nb_valid_passwords)
