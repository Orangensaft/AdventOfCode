from utils.puzzle import Puzzle
from copy import copy


class Day2(Puzzle):
    YEAR = 2024
    DAY = 2

    @staticmethod
    def _copy_pop(number_list: list[int], index: int) -> list[int]:
        # Pop is in place by default, create a copy first
        out = copy(number_list)
        out.pop(index)
        return out

    @staticmethod
    def is_monotonic(number_list: list[int]) -> bool:
        return (
            sorted(number_list) == number_list
            or sorted(number_list) == number_list[::-1]
        )

    @staticmethod
    def has_valid_gaps(number_list: list[int]) -> bool:
        # make sure gaps between numbers are >=1 and <=3
        for i in range(len(number_list) - 1):
            gap = abs(number_list[i] - number_list[i + 1])
            if gap < 1 or gap > 3:
                return False
        return True

    @staticmethod
    def is_safe_report(number_list: list[int]) -> bool:
        return Day2.is_monotonic(number_list) and Day2.has_valid_gaps(number_list)

    @staticmethod
    def is_safe_by_optional_dropping(number_list: list[int]) -> bool:
        if Day2.is_safe_report(number_list):
            return True  # Is safe as is
        for i in range(len(number_list)):
            if Day2.is_safe_report(Day2._copy_pop(number_list, i)):
                return True
        return False

    def part1(self):
        """
        Basic idea: If the report is safe, it has to be monotonically increasing or decreasing,
        aswell as having gaps >=1 amd <=3

        Increasing and decreasing can easily be checked by checking if the list is already sorted (increasing or decreasing)
        """
        reports = [[int(j) for j in i.split(" ")] for i in self.input.split("\n")]
        return len(list(filter(Day2.is_safe_report, reports)))

    def part2(self):
        """
        Same as part1 but dropping a single element before doing checks is allowed now.
        Idea: First check if report is good as is. If not: Try dropping alle indices once to see if any of that makes
        it safe.
        """
        reports = [[int(j) for j in i.split(" ")] for i in self.input.split("\n")]
        return len(list(filter(Day2.is_safe_by_optional_dropping, reports)))
