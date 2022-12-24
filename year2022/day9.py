import math

from utils.puzzle import Puzzle
import matplotlib.pyplot as plt


class Rope:
    def __init__(self, starting_pos, length=2):
        self.parts = [starting_pos for i in range(length)]  # (int, int)
        self.tail_positions = set()
        self.tail_positions.add(starting_pos)

    def get_new_tip_pos(self, direction: str):
        head = self.parts[0]
        if direction == "U":
            return head[0], head[1] + 1
        if direction == "D":
            return head[0], head[1] - 1
        if direction == "L":
            return head[0] - 1, head[1]
        if direction == "R":
            return head[0] + 1, head[1]

    def move_cmd(self, cmd: str):
        direction, amount = cmd.split(" ")
        amount = int(amount)
        for i in range(amount):
            self.move(direction)

    def move(self, direction: str):
        self.parts[0] = self.get_new_tip_pos(direction)  # will move there

        for i in range(1, len(self.parts)):
            # check dist with old pos
            cur = self.parts[i]
            prev = self.parts[i - 1]
            dx = prev[0] - cur[0]
            dy = prev[1] - cur[1]
            if abs(dx) > 1 or abs(dy) > 1:
                # move the knot
                x_sign = -1 if dx < 0 else 1
                y_sign = -1 if dy < 0 else 1

                if dx == 0:  # only y
                    # move cur one step in y direction
                    cur = cur[0], cur[1] + y_sign
                    self.parts[i] = cur

                elif dy == 0:
                    # move cur one step in x direction
                    cur = cur[0] + x_sign, cur[1]
                    self.parts[i] = cur

                else:
                    # dx and dy != 0 --> moved diag
                    cur = cur[0] + x_sign, cur[1] + y_sign
                    self.parts[i] = cur

        self.tail_positions.add(self.parts[-1])  # track position of tail

    def plot(self):
        all_pos = self.tail_positions
        x, y = zip(*all_pos)
        plt.scatter(x, y, marker=",")
        plt.show()

    @staticmethod
    def get_distance(x, y, x1, y1):
        return math.floor(math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2))


class Day9(Puzzle):
    YEAR = 2022
    DAY = 9

    def part1(self):
        r = Rope((0, 0))
        for cmd in self.input.split("\n"):
            r.move_cmd(cmd)
        return len(r.tail_positions)

    def part2(self):
        r = Rope((0, 0), 10)
        for cmd in self.input.split("\n"):
            r.move_cmd(cmd)
        return len(r.tail_positions)
