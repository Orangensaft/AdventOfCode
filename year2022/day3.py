import string
from collections import Counter
from copy import deepcopy

from utils.puzzle import Puzzle

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


class Day3(Puzzle):
    YEAR = 2022
    DAY = 3

    def part1(self):
        bags = self.input.split("\n")
        total = 0
        for bag in bags:
            total += get_bag_prio(bag)
        return total

    def part2(self):
        bags = self.input.split("\n")
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

        return total
