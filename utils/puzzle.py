from abc import ABC
from time import time
from utils import read_input


class Puzzle(ABC):
    YEAR = -1
    DAY = -1

    def __init__(self):
        if -1 in [self.DAY, self.YEAR]:
            self.part1 = lambda: "DAY/YEAR missing"
            self.part2 = lambda: "DAY/YEAR missing"
            self.input = ""
            return
        self.input = read_input(self.YEAR, self.DAY).strip()

    def __measure(self, f: callable):
        start = time()
        r = f()
        total = (time() - start) * 1000
        return r, total

    def run(self):

        p1, ms1 = self.__measure(self.part1)
        p2, ms2 = self.__measure(self.part2)
        print(f"{self.YEAR}.{self.DAY}.1:\t{p1}\t\t\t\tin {ms1:.2f}ms")
        print(f"{self.YEAR}.{self.DAY}.2:\t{p2}\t\t\t\tin {ms2:.2f}ms")

    def part1(self):
        return "-"

    def part2(self):
        return "-"
