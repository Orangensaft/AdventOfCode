from utils.puzzle import Puzzle


class Day1(Puzzle):
    YEAR = 2024
    DAY = 1

    @staticmethod
    def calculate_dists(list1, list2) -> int:
        total = 0
        for i in range(len(list1)):
            item_1, item_2 = list1[i], list2[i]
            dist = abs(item_1 - item_2)
            total += dist
        return total

    @staticmethod
    def sort_lists(list1, list2):
        list1 = sorted(list1)
        list2 = sorted(list2)
        return list1, list2

    def part1(self):
        # get the two lists
        lists = self.get_lists(self.input)
        list1, list2 = self.sort_lists(lists[0], lists[1])
        total = self.calculate_dists(list1, list2)
        return total

    def part2(self):
        list1, list2 = self.get_lists(self.input)
        total = 0
        for i in list1:
            total += i * list2.count(i)
        return total

    def get_lists(self, puzzle_input):
        # get the puzzle input and split into two lists
        list1, list2 = [], []
        for line in puzzle_input.split("\n"):
            a, b = line.split("   ")
            list1.append(int(a))
            list2.append(int(b))
        return list1, list2
