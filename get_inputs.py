import requests
import pathlib
import sys
import os

# grab all days
def grab(year, day):
    token = os.environ.get("AOC_TOKEN", "")
    r = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token}
    )
    if r.status_code == 200:
        return r.content.decode()
    else:
        return None


def save(year, day, target):
    content = grab(year, day)
    if content is not None:
        target.write_text(content)
    else:
        print(f"{year}/{day} not available! Bye!")
        sys.exit(0)


def save_all(force=False):
    for year in range(2015, 2024):
        for day in range(1, 26):
            p = pathlib.Path(f"inputs") / str(year) / str(day)
            p.parent.mkdir(
                parents=True, exist_ok=True
            )  # make sure that parent dir exists
            if p.exists() and not force:
                print(f"Skipping {year}/{day} as it exists. --force to override")
                continue
            else:
                save(year, day, p)
                print(f"Saved {year}/{day}")
    print("Done")


if __name__ == "__main__":
    save_all()
