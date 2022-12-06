from utils.puzzle import Puzzle


class Day1(Puzzle):
    YEAR = 2022
    DAY = 1

    def fill_bags(self):
        bags = []
        cur = 0
        for i in self.input.split("\n"):
            if i == "":
                bags.append(cur)
                cur = 0
            else:
                cur += int(i)
        return bags

    def part1(self):
        return max(self.fill_bags())

    def part2(self):
        return sum(sorted(self.fill_bags())[::-1][0:3])


if __name__ == "__main__":
    Day1().run()
