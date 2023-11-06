from year2017.day1 import part1_sum, part2_sum


def test_part1_sum_example_1():
    assert part1_sum("1122") == 3


def test_part1_sum_example_2():
    assert part1_sum("1111") == 4


def test_part1_sum_example_3():
    assert part1_sum("1234") == 0


def test_part1_sum_example_4():
    assert part1_sum("91212129") == 9


def test_part2_sum_examples():
    tests = [("1212", 6), ("1221", 0), ("123425", 4), ("123123", 12), ("12131415", 4)]
    for inp, result in tests:
        assert part2_sum(inp) == result
