import itertools

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_expenses = f.read().splitlines()

    expenses = [int(raw_expense) for raw_expense in raw_expenses]
    all_tuples = itertools.product(*[expenses, expenses])

    for tuple in all_tuples:
        nb1 = tuple[0]
        nb2 = tuple[1]

        if nb1 + nb2 == 2020:
            res = nb1 * nb2
            break

    print(res)
