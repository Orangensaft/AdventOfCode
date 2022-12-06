from utils import read_input


def fully_contains(range1, range2):
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        # range2 is in range1
        return True
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        # range1 is in range2
        return True
    return False


def overlaps_partly(range1, range2):
    # too lazy to write down all the combinations
    size = max(range1[1], range2[1])
    field = [0 for i in range(size + 1)]
    for i in range(range1[0], range1[1] + 1):
        field[i] += 1
    for i in range(range2[0], range2[1] + 1):
        field[i] += 1
    overlaps = filter(lambda x: x > 1, field)
    return len(list(overlaps)) > 0


def string_to_range(s):
    return [int(i) for i in s.split("-")]


def parse_line(line):
    l, r = line.split(",")
    range1 = string_to_range(l)
    range2 = string_to_range(r)
    return range1, range2


def part1():
    inp = read_input(2022, 4).strip().split("\n")
    ranges = [parse_line(l) for l in inp]
    doubles = [i for i in ranges if fully_contains(i[0], i[1])]
    print(len(doubles))


def part2():
    inp = read_input(2022, 4).strip().split("\n")
    ranges = [parse_line(l) for l in inp]
    partly = [i for i in ranges if overlaps_partly(i[0], i[1])]
    print(len(partly))


if __name__ == "__main__":
    part1()
    part2()
