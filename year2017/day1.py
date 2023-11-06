from utils.puzzle import Puzzle


def part1_sum(input_str: str) -> int:
    total = 0
    for i in range(len(input_str) - 1):
        cur = input_str[i]
        nxt = input_str[i + 1]
        if cur == nxt:
            total += int(cur)
    if input_str[-1] == input_str[0]:
        total += int(input_str[0])
    return total


def part2_sum(inpt_str: str) -> int:
    total = 0
    length = len(inpt_str)
    step_size = length // 2
    for i in range(length):
        if inpt_str[i] == inpt_str[(i + step_size) % length]:
            total += int(inpt_str[i])
    return total


class Day1(Puzzle):
    YEAR = 2017
    DAY = 1

    def part1(self):
        return part1_sum(self.input)

    def part2(self):
        return part2_sum(self.input)
