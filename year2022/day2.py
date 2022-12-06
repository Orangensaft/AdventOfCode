from utils.puzzle import Puzzle

WINNING = {"A": "Y", "B": "Z", "C": "X"}


DRAW = {"A": "X", "B": "Y", "C": "Z"}

LOOSE = {"A": "Z", "B": "X", "C": "Y"}


def get_hand_score(t):
    if t in ["X", "A"]:
        return 1
    if t in ["Y", "B"]:
        return 2
    else:
        return 3


def get_score_total(opponent, me):
    if WINNING[opponent] == me:
        return 6 + get_hand_score(me)

    if DRAW[opponent] == me:
        return 3 + get_hand_score(me)

    return get_hand_score(me)


def check_line(line):
    o, m = line.split(" ")
    return get_score_total(o, m)


def follow_guide(lines):
    total = 0
    for l in lines:
        total += check_line(l)
    return total


def part_2_points(opponent, target):
    if target == "X":  # loosing
        me = LOOSE[opponent]
        return get_hand_score(me)

    elif target == "Y":  # draw
        me = DRAW[opponent]
        return get_hand_score(me) + 3
    else:
        me = WINNING[opponent]
        return get_hand_score(me) + 6


class Day2(Puzzle):
    YEAR = 2022
    DAY = 2

    def part1(self):
        return follow_guide(self.input.split("\n"))

    def part2(self):
        total = 0
        for inp in self.input.split("\n"):
            opponent, target = inp.split(" ")
            total += part_2_points(opponent, target)
        return total
