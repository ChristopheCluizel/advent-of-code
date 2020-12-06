from collections import Counter


def load_groups_answers():
    with open("./input.txt", "r") as f:
        return f.read().replace("\n\n", "|").replace("\n", " ").split("|")


def count_answers(groups_answers):
    res = []
    for group_answers in groups_answers:
        nb_yes_responses = 0
        individual_answers = group_answers.split(" ")
        group_size = len(individual_answers)

        group_answers = group_answers.replace(" ", "")
        counter_res = Counter(group_answers)

        for key, value in counter_res.items():
            if value == group_size:
                nb_yes_responses += 1
        res.append(nb_yes_responses)

    return res


if __name__ == "__main__":
    groups_answers = load_groups_answers()
    answers = count_answers(groups_answers)

    print(sum(answers))
