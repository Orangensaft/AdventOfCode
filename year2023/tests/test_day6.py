import operator
from functools import reduce

from year2023.day6 import calc_distance, get_all_winning_distances, parse_races

EXAMPLE = """Time:      7  15   30
Distance:  9  40  200"""

def test_distance_travelled():
    assert calc_distance(0,7) == 0
    assert calc_distance(1,7) == 6
    assert calc_distance(2,7) == 10
    assert calc_distance(3,7) == 12
    assert calc_distance(4,7) == 12
    assert calc_distance(5,7) == 10
    assert calc_distance(6,7) == 6
    assert calc_distance(7,7) == 0


def test_get_times_to_win():
    assert get_all_winning_distances(7, 9) == [2,3,4,5]


def test_parse_races():
    races = parse_races(EXAMPLE)
    assert len(races) == 3
    assert races[1] == (15,40)


def test_full_example():
    races = parse_races(EXAMPLE)
    win_counts = []
    for time, distance in races:
        win_counts.append(
            len(
                get_all_winning_distances(time, distance)
            )
        )
    assert len(win_counts) == 3
    # Same as foldl with multiplication
    assert reduce(operator.mul,win_counts, 1) == 288

