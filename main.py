import abc
import argparse
import datetime
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


def run_all(year_to_run: int | None = None):
    if year_to_run is None:
        year_to_run = range(2015, 2024)
    else:
        year_to_run = [year_to_run]
    for year in year_to_run:
        print(f"----Year {year}----")
        for day in range(1, 26):
            try:
                run(year, day)
            except ModuleNotFoundError:
                continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int)
    parser.add_argument("-d", "--day", type=int)
    parser.add_argument("-t", "--today", action="store_true")
    args = parser.parse_args()
    if args.today:
        # only run today
        today = datetime.date.today()
        args.year = today.year
        args.day = today.day
    if args.day is not None and args.year is not None:
        # Run given year+day
        print(f"Running {args.year}.{args.day}")
        try:
            run(args.year, args.day)
        except ModuleNotFoundError:
            print("Not implemented :(")
    elif args.year is not None:
        # Run given year
        run_all(args.year)
    else:
        # Run everything
        run_all()
