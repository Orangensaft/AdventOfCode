from utils.puzzle import Puzzle
from .day1 import Day1
from .day2 import Day2


def run():
    print("----- 2015 -----")
    v = globals()
    for key, cls in v.items():
        if key.startswith("Day") and issubclass(cls, Puzzle):
            cls().run()
