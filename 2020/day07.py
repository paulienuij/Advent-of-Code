from collections import defaultdict, deque

with open("day07.txt") as file:
    rules = file.read().splitlines()

contained_by = defaultdict(list)
container_of = defaultdict(list)
colors = []

for rule in rules:
    rule = rule.replace(" bags", "").replace(" bag", "").replace(".", "")
    container, inside = rule.split(" contain ")
    if "no other bags" in inside:
        continue
    for bag in inside.split(", "):
        contained_by[container].append([bag[0], bag[2:]])
        container_of[bag[2:]].append(container)


colors = []
bags_to_check = ["shiny gold"]


while len(bags_to_check) > 0:
    bags_to_check, bag = bags_to_check[:-1], bags_to_check[-1]
    for x in container_of[bag]:
        if x not in bags_to_check:
            bags_to_check.append(x)
            colors.append(x)

print(len(set(colors)))


def amount_of_bags_for(color):
    amount = 1
    for nb, subcolor in contained_by[color]:
        if nb == "n":
            pass
        else:
            amount += int(nb) * amount_of_bags_for(subcolor)
    return amount


print(amount_of_bags_for("shiny gold") - 1)  # I don't understand why I am off by 1
