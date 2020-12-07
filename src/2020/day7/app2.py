def load_rules():
    with open("./input.txt", "r") as f:
        return f.read().splitlines()


def extract_bag(raw_bag):
    formatted_bag = raw_bag.strip()
    splits = formatted_bag.split(" ")
    number = int(splits[0].strip())
    bag = " ".join(splits[1:])

    if bag[-1] == "s":
        bag = bag[:-1]

    res = []
    for i in range(0, number):
        res.append(bag)

    return res


def get_bags(rule):
    splits = rule.split("contain")
    key = splits[0].strip()[:-1]
    raw_bags = splits[1]

    bags = []
    if "no other bags" in raw_bags:
        bags = []
    else:
        bags_splits = raw_bags.replace(".", "").split(",")
        for bag in bags_splits:
            temp_res = extract_bag(bag)
            for temp in temp_res:
                bags.append(temp)

    return key, bags


def create_dict(rules):
    res = {}
    for rule in rules:
        key, bags = get_bags(rule)
        res[key] = bags

    return res


def count_bags(_dict, bags):
    if len(bags) == 0:
        return 0
    else:
        count = len(bags)
        for bag in bags:
            res = count_bags(_dict, _dict[bag])
            count += res
        return count


if __name__ == "__main__":
    rules = load_rules()
    _dict = create_dict(rules)

    res = count_bags(_dict, ["shiny gold bag"])

    print(res - 1)
