import string
from collections import Counter
from copy import deepcopy

from utils import read_input

ITEMS = string.ascii_lowercase + string.ascii_uppercase


def item_to_prio(i: str):
    return ITEMS.find(i) + 1


def get_compartments(items: str):
    l = len(items) // 2
    return items[:l], items[l:]


def get_double(items: str):
    left, right = get_compartments(items)
    # dont count doubles
    left = "".join(set(left))
    right = "".join(set(right))
    counts = Counter(left + right)
    item, count = counts.most_common(1)[0]
    return item


def get_bag_prio(items: str):
    item = get_double(items)
    return item_to_prio(item)


def find_item(group):
    c = Counter("".join(group))
    return c.most_common(1)[0][0]


def part1():
    bags = read_input(2022, 3).strip().split("\n")
    total = 0
    for bag in bags:
        total += get_bag_prio(bag)
    print(total)


def part2():
    bags = read_input(2022, 3).strip().split("\n")
    groups = []
    group = []
    for bag in bags:
        group.append("".join(set(bag)))
        if len(group) == 3:
            groups.append(deepcopy(group))
            group = []

    total = 0

    for group in groups:
        item = find_item(group)
        prio = item_to_prio(item)
        total += prio

    print(total)


if __name__ == "__main__":
    part1()
    part2()
