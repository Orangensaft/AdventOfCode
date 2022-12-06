from pathlib import Path


def read_input(year: int, day: int):
    p = Path("inputs") / str(year) / str(day)
    return p.read_text()
