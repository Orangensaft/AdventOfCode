from utils.puzzle import Puzzle


class Day1(Puzzle):
    YEAR = 2015
    DAY = 1

    def part1(self):
        return self.input.count("(") - self.input.count(")")

    def part2(self):
        level = 0
        for i, c in enumerate(self.input):
            if c == "(":
                level += 1
            else:
                level -= 1
                if level < 0:
                    return i + 1
