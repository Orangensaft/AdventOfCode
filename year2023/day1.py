from utils.puzzle import Puzzle


REPLACE_NUMBERS = {
    "twone": "21",
    "nineight": "98",
    "oneight": "18",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_numbers(s: str) -> int:
    for key, val in REPLACE_NUMBERS.items():
        s = s.replace(key, val)
    return get_calibration_number(s)


def count_part_2(lines):
    total = 0
    for line in lines:
        to_add = replace_numbers(line)
        total += to_add
    return total


def get_calibration_number(line):
    clean = [int(i) for i in line if i.isnumeric()]
    to_add = 10 * clean[0] + clean[-1]
    return to_add


class Day1(Puzzle):
    YEAR = 2023
    DAY = 1

    def part1(self):
        lines = self.input.split("\n")
        total = 0
        for line in lines:
            clean = [int(i) for i in line if i.isnumeric()]
            total += 10 * clean[0] + clean[-1]
        return total

    def part2(self):
        lines = self.input.split("\n")
        return count_part_2(lines)
