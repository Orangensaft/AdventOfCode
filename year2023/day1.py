from utils.puzzle import Puzzle



def replace_nums(s: str) -> str:
    nums = ["!!!", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replacements = []
    for start in range(len(s)):
        for end in range(start, len(s)+1):
            cur = s[start:end]
            if cur in nums:
                replacements.append(cur)
                break
    for replacement in replacements:
        s = s.replace(replacement, str(nums.index(replacement)))
    return s

class Day1(Puzzle):
    YEAR = 2023
    DAY = 1

    def part1(self):
        lines = self.input.split("\n")
        total = 0
        for line in lines:
            clean = [int(i) for i in line if i.isnumeric()]
            total += 10*clean[0] + clean[-1]
        return total


    def part2(self):
        #lines = self.input.split("\n")
        lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split("\n")
        total = 0
        for line in lines:
            clean_line = replace_nums(line)

        return total