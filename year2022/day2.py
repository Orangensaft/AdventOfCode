from utils import read_input

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


def part1():
    inputs = read_input(2022, 2).strip().split("\n")
    print(follow_guide(inputs))


def part2():
    total = 0
    inputs = read_input(2022, 2).strip().split("\n")
    for inp in inputs:
        opponent, target = inp.split(" ")
        total += part_2_points(opponent, target)
    print(total)


if __name__ == "__main__":
    part1()
    part2()
