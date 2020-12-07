import re


def load_rules():
    with open("./input.txt", "r") as f:
        return f.read().splitlines()


def extract_bag(raw_bag):
    formatted_bag = raw_bag.strip()
    find = re.search(r"(\b[^\d]+\b)", formatted_bag)

    if find:
        word = find.group(0).strip()
        if word[-1] == "s":
            word = word[:-1]
        return word


def get_bags(rule):
    splits = rule.split("contain")
    key = splits[0].strip()[:-1]
    raw_bags = splits[1]

    if "no other bags" in raw_bags:
        bags = []
    else:
        bags_splits = raw_bags.replace(".", "").split(",")
        bags = [extract_bag(bag) for bag in bags_splits]

    return key, bags


def create_dict(rules):
    res = {}
    for rule in rules:
        key, bags = get_bags(rule)
        res[key] = bags

    return res


def find_shiny_bag(_dict, bags):
    if len(bags) == 0:
        return False
    elif "shiny gold bag" in bags:
        return True
    else:
        all_res = []
        for bag in bags:
            res = find_shiny_bag(_dict, _dict[bag])
            all_res.append(res)
        if True in all_res:
            return True
        else:
            return False


if __name__ == "__main__":
    rules = load_rules()
    _dict = create_dict(rules)

    all_res = []
    for key, value in _dict.items():
        res = find_shiny_bag(_dict, value)
        if res:
            all_res.append(key)

    print(len(all_res))
