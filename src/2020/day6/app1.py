def load_groups_answers():
    with open("./input.txt", "r") as f:
        return f.read().replace("\n\n", "|").replace("\n", "").split("|")


def count_answers(groups_answers):
    res = []
    for group_answers in groups_answers:
        unique_answers = set(group_answers)
        res.append(len(unique_answers))

    return res


if __name__ == "__main__":
    groups_answers = load_groups_answers()
    answers = count_answers(groups_answers)

    print(sum(answers))
