from importlib import import_module
from utils.puzzle import Puzzle


def run(year: int, day: int):
    day_module = import_module(f"year{year}.day{day}")
    cls: Puzzle = getattr(day_module, f"Day{day}")
    cls().run()


def run_all():
    for year in range(2015, 2024):
        print(f"----Year {year}----")
        for day in range(1,26):
            try:
                run(year, day)
            except ModuleNotFoundError:
                continue


if __name__ == "__main__":
    run_all()
