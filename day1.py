from utils import read_input


def fill_bags():
    inputs = read_input(2022, 1).split("\n")
    bags = []
    cur = 0
    for i in inputs:
        if i == "":
            bags.append(cur)
            cur = 0
        else:
            cur += int(i)
    return bags


def part1():
    return max(fill_bags())


def part2():
    return sum(sorted(fill_bags())[::-1][0:3])


if __name__ == "__main__":
    print(part1())
    print(part2())
