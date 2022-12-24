from utils.puzzle import Puzzle
from year2022.day1 import Day1
from year2022.day2 import Day2
from year2022.day3 import Day3
from year2022.day4 import Day4
from year2022.day5 import Day5
from year2022.day6 import Day6
from year2022.day7 import Day7
from year2022.day8 import Day8
from year2022.day9 import Day9
from year2022.day10 import Day10


def run():
    print("----- 2022 -----")
    v = globals()
    for key, cls in v.items():
        if key.startswith("Day") and issubclass(cls, Puzzle):
            cls().run()
