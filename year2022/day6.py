from utils import read_input
from utils.puzzle import Puzzle


class RingBuffer:
    def __init__(self, size):
        self.content = []
        self.size = size

    def push(self, item: object):
        if len(self.content) < self.size:
            self.content.append(item)
        else:
            self.content.pop(0)
            self.content.append(item)

    def get_content(self):
        return self.content


class MarkerChecker:
    def __init__(self, buffersize=4):
        self.buffer = RingBuffer(buffersize)

    def push(self, char: str):
        self.buffer.push(char)
        return self.has_no_double()

    def has_no_double(self):
        return len(set(self.buffer.get_content())) == self.buffer.size

    def get_marker(self):
        return "".join(self.buffer.get_content())

    def __str__(self):
        return self.get_marker()

    def __repr__(self):
        return f"<Marker {self} - Is Marker: {self.has_no_double()}"


def get_marker(signal: str, marker_size: int):
    m = MarkerChecker(marker_size)
    for i, c in enumerate(signal):
        if m.push(c):
            return i + 1  # because of zero indexing
    return -1


class Day6(Puzzle):
    YEAR = 2022
    DAY = 6

    def part1(self):
        return get_marker(self.input, 4)

    def part2(self):
        return get_marker(self.input, 14)
