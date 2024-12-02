from year2023.day8 import read_nodes, process_commands, all_arrived, process_ghost

EXAMPLE = """AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""


EXAMPLE_TWO = """AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def test_process_commands_example_1():
    nodes = read_nodes(EXAMPLE.split("\n"))
    steps = process_commands(nodes, "RL")
    assert steps == 2


def test_process_commands_example_2():
    nodes = read_nodes(EXAMPLE_TWO.split("\n"))
    steps = process_commands(nodes, "LLR")
    assert steps == 6


def test_all_arrived():
    assert all_arrived(["AAZ", "ZZZ", "ACZ"])
    assert not all_arrived(["ZZA", "ABC"])
    assert not all_arrived(["AAA", "BBB"])


def test_part2():
    maze = """11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    commands = "LR"
    nodes = read_nodes(maze.split("\n"))

    assert process_ghost(nodes, commands) == 6
