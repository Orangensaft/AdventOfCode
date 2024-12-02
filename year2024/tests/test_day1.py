from year2024.day1 import Day1

TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_get_lists():
    d = Day1()
    list1, list2 = d.get_lists(TEST_INPUT)
    assert len(list1) == len(list2) == 6


def test_sort_lists():
    d = Day1()
    list1, list2 = d.get_lists(TEST_INPUT)
    list1, list2 = d.sort_lists(list1, list2)
    assert list1[0] == 1
    assert list2[0] == 3
    assert list1[-1] == 4
    assert list2[-1] == 9


def test_calculate_dists():
    d = Day1()
    list1, list2 = d.get_lists(TEST_INPUT)
    list1, list2 = d.sort_lists(list1, list2)
    total = d.calculate_dists(list1, list2)
    assert total == 11
