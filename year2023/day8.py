from utils.puzzle import Puzzle
from math import lcm

"""
AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""


def read_nodes(node_lines: [str]) -> dict:
    out = {}
    for line in node_lines:
        node, others = (
            line.replace(" ", "").replace("(", "").replace(")", "").split("=")
        )
        others = others.split(",")
        out[node] = others
    return out


def single_step(nodes, current, command):
    left, right = nodes[current]
    if command == "L":
        return left
    else:
        return right


def process_commands(nodes: dict, commands: str, part2=False, cur="AAA"):
    total_steps = 0

    while True:
        if not part2:
            if cur == "ZZZ":
                break
        else:
            if cur.endswith("Z"):
                break
        for command in commands:
            cur = single_step(nodes, cur, command)
            total_steps += 1
    return total_steps


def all_arrived(current_locations: [str]):
    return all([i.endswith("Z") for i in current_locations])


def process_ghost(nodes, commands):
    current_nodes = [node for node in nodes if node.endswith("A")]
    steps = [process_commands(nodes, commands, True, n) for n in current_nodes]
    # the first time they all arrive at the same stop should be the least common multiple of the distances
    return lcm(*steps)  # Fuck yeah python builtins


class MazeWalker(Puzzle):
    DAY = 8
    YEAR = 2023

    def part1(self):
        commands = self.input.split("\n")
        maze = commands[2:]
        commands = commands[0]
        nodes = read_nodes(maze)
        return process_commands(nodes, commands)

    def part2(self):
        commands = self.input.split("\n")
        maze = commands[2:]
        commands = commands[0]
        nodes = read_nodes(maze)
        return process_ghost(nodes, commands)
