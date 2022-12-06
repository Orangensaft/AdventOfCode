from utils import read_input
from utils.puzzle import Puzzle


class CrateMover9000:
    def __init__(self):
        lines = read_input(2022, 5).split("\n")
        stacks = lines[:8][::-1]  # to fill the stack more easy
        self.stacks = [[] for i in range(10)]
        for stackline in stacks:
            for i in range(9):
                start = 3 * i + i
                end = start + 3
                current = stackline[start:end][1:2]
                if current != " ":
                    self.stacks[i + 1].append(current)
        self.commands = []
        for cmd in lines[9:]:
            if cmd:
                self.commands.append(self.parse_commands(cmd))

    def parse_commands(self, line: str):
        _, count, _, from_idx, _, to_idx = line.split(" ")
        return int(count), int(from_idx), int(to_idx)

    def execute_commands(self):
        for count, from_id, to_idx in self.commands:
            self.move(count, from_id, to_idx)
        return self

    def move(self, count: int, from_idx: int, to_idx: int):
        for i in range(count):
            elem = self.stacks[from_idx].pop()
            self.stacks[to_idx].append(elem)

    def print_stacks(self):
        i = 1
        for stack in self.stacks[1:]:
            print(f"{i}: {stack}")
            i += 1

    def get_top_crates(self):
        out = ""
        for stack in self.stacks[1:]:
            if not len(stack):
                out += "."
            else:
                out += stack[-1]
        return out


class CrateMover9001(CrateMover9000):
    def move(self, count: int, from_id: int, to_idx: int):
        to_move = []
        for i in range(count):
            to_move.append(self.stacks[from_id].pop())
        for i in range(count):
            self.stacks[to_idx].append(to_move.pop())

    def execute_commands(self):
        for count, from_id, to_idx in self.commands:
            self.move(count, from_id, to_idx)
        return self


class Day5(Puzzle):
    YEAR = 2022
    DAY = 5

    def part1(self):
        return CrateMover9000().execute_commands().get_top_crates()

    def part2(self):
        return CrateMover9001().execute_commands().get_top_crates()
