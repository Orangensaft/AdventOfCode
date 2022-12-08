from utils.datastructures import Field2D
from utils.puzzle import Puzzle
from functools import lru_cache

VISIBLE = 1
INVISIBLE = 0
UNKNOWN = -1

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
ANY = 5


class Forest:
    def __init__(self, size=100):
        self.size = size
        self.trees = Field2D(size, size)
        self.visible = Field2D(size, size, False)

    @staticmethod
    def from_input(puzzle_input: str):
        size = len(puzzle_input.split("\n")[0])
        puzzle_input = puzzle_input.replace("\n", "").strip()
        f = Forest(size)
        f.trees.field = []
        for i in puzzle_input:
            f.trees.field.append(int(i))
        return f

    def get_visibilities(self):
        for y in range(self.size):
            for x in range(self.size):
                self.visible[x, y] = self.get_visibility(x, y)

    def get_visibility(self, x, y):
        my_height = self.trees[x, y]
        left = [self.trees[xi, y] for xi in range(x - 1, -1, -1)]
        right = [self.trees[xi, y] for xi in range(x + 1, self.size)]
        up = [self.trees[x, yi] for yi in range(y - 1, -1, -1)]
        down = [self.trees[x, yi] for yi in range(y + 1, self.size)]

        def is_vis(l):
            return all([i < my_height for i in l])

        return is_vis(left) or is_vis(right) or is_vis(up) or is_vis(down)

    def get_visible_trees(self, x, y, direction):
        RANGES = {
            LEFT: range(x - 1, -1, -1),
            RIGHT: range(x + 1, self.size),
            UP: range(y - 1, -1, -1),
            DOWN: range(y + 1, self.size),
        }

        visible = 1
        my_height = self.trees[x, y]
        if direction in [LEFT, RIGHT]:
            for xi in RANGES[direction]:
                if self.trees[xi, y] < my_height:
                    visible += 1
                else:
                    return visible

        if direction in [UP, DOWN]:
            for yi in RANGES[direction]:
                if self.trees[x, yi] < my_height:
                    visible += 1
                else:
                    return visible

        return visible - 1

    def get_scenic_score(self, x, y):
        total = 1
        for d in [UP, DOWN, LEFT, RIGHT]:
            total *= self.get_visible_trees(x, y, d)
        return total

    def get_best_place(self):
        best = 0
        for x in range(self.size):
            for y in range(self.size):
                score = self.get_scenic_score(x, y)
                if score > best:
                    best = score
        return best

    def plot_forest(self):
        import matplotlib.pyplot as plt

        coords = []
        for x in range(self.size):
            for y in range(self.size):
                vis = self.visible[x, y]
                coords.append((x, y, "g" if vis else "black"))

        x, y, col = zip(*coords)
        plt.scatter(x, y, color=col)
        plt.gca().invert_yaxis()  # because origin is top left
        plt.show()


class Day8(Puzzle):
    YEAR = 2022
    DAY = 8

    def part1(self):
        f = Forest.from_input(self.input)
        f.get_visibilities()
        return f.visible.count(True)

    def part2(self):
        f = Forest.from_input(self.input)
        return f.get_best_place()
