from year2023.day1 import count_part_2, replace_numbers


def test_part2_examples():
    data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    total = count_part_2(data.split("\n"))
    assert total == 281


def test_part2_parse_special():
    data = "zoneight234"
    assert replace_numbers(data) == 14


def test_part2_parse_random():
    data = "4nineeightseven2"
    assert replace_numbers(data) == 42


def test_part2_unknown_case_1():
    data = "eighthree"
    assert replace_numbers(data) == 83


def test_part2_unknown_case_2():
    data = "sevenine"
    assert replace_numbers(data) == 79
