from utils import read_input


class Cranes:
    def __init__(self):
        lines = read_input(2022, 5).split("\n")
        stacks = lines[:8][::-1]  # to fill the stack more easy
        self.stacks = [[] for i in range(8)]
        for stackline in stacks:
            for i in range(9):
                start = i+3*i
                end = start+3
                current = stackline[start:end]
                print(current)