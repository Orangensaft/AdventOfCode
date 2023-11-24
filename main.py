import abc
from importlib import import_module
from utils.puzzle import Puzzle


def run(year: int, day: int):
    day_module = import_module(f"year{year}.day{day}")
    for content in dir(day_module):
        cls = getattr(day_module, content)
        if type(cls) is Puzzle:  # Ignore the puzzle class import
            continue
        # As we are using a subclass of an abstract class, class will be abc.ABCMeta
        # and issubclass(cls, Puzzle) will be false
        if type(cls) is abc.ABCMeta and cls.__base__ == Puzzle:
            cls().run()


def run_all():
    for year in range(2015, 2024):
        print(f"----Year {year}----")
        for day in range(1, 26):
            try:
                run(year, day)
            except ModuleNotFoundError:
                continue


if __name__ == "__main__":
    run_all()
