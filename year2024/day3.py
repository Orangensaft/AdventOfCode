from utils.puzzle import Puzzle

import re

REGEX = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
REGEX_DO = re.compile(r"do\(\)")
REGEX_DONT = re.compile(r"don\'t\(\)")


class Day3(Puzzle):
    YEAR = 2024
    DAY = 3

    def part1(self):
        return Day3.complete_process(self.input)

    def part2(self):
        # collect the starts of dont blocks
        donts = []
        for group in REGEX_DONT.finditer(self.input):
            donts.append(group.start())

        # collect the start of do blocks
        dos = []
        for group in REGEX_DO.finditer(self.input):
            dos.append(group.start())

        # collect the start of mul blocks with their values
        muls = {}
        for group in REGEX.finditer(self.input):
            muls[group.start()] = group.groups()

        # iterate through the string and depending on whats at the index to stuff
        skip = False  # Flag is true when inside a dont block, "at the beginning of the program, mul instructions are enabled."
        total = 0
        for i in range(len(self.input)):
            if i in donts:  # Start of a dont block
                skip = True
            if i in dos:  # Start of a do block
                skip = False
            if (
                i in muls and not skip
            ):  # We found a mult and are outside of a dont block
                group = muls[i]
                total += int(group[0]) * int(group[1])
        return total

    @staticmethod
    def complete_process(input_string: str) -> int:
        groups = REGEX.findall(input_string)
        total = 0
        for a, b in groups:
            total += int(a) * int(b)
        return total
