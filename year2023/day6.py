import operator
from functools import reduce

from utils.puzzle import Puzzle


def calc_distance(held_down: int, max_time: int) -> int:
    return (max_time - held_down) * held_down


def get_all_winning_distances(time: int, distance_to_beat: int) -> [int]:
    out = []
    for i in range(time):  # could be solved mathematically. But meh.
        if calc_distance(i, time) > distance_to_beat:
            out.append(i)
    return out


def parse_races(input_str: str, part_2=False) -> [(int, int)]:
    timeline, distance_line = input_str.split("\n")
    if part_2:
        times = [int(timeline.split("Time:")[-1].replace(" ", ""))]
        distances = [int(distance_line.split("Distance:")[-1].replace(" ", ""))]
    else:
        times = [int(i) for i in timeline.split("Time:")[-1].split()]
        distances = [int(i) for i in distance_line.split("Distance:")[-1].split()]
    return list(zip(times, distances))


class BoatRacer5000(Puzzle):
    DAY = 6
    YEAR = 2023

    def part1(self):
        races = parse_races(self.input)
        win_counts = []
        for time, distance in races:
            win_counts.append(len(get_all_winning_distances(time, distance)))
        return reduce(operator.mul, win_counts, 1)

    def part2(self):
        races = parse_races(self.input, part_2=True)
        assert len(races) == 1
        time, distance = races[0]
        # Bruteforce all the way this year
        winning = len(get_all_winning_distances(time, distance))
        return winning
