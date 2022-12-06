from utils import read_input


class MarkerChecker:
    def __init__(self):
        self.content = []

    def push(self, char: str):
        if len(self.content) < 4:
            self.content.append(char)
        else:
            self.content.pop(0)
            self.content.append(char)
        return self.has_no_double()

    def has_no_double(self):
        return len(set(self.content)) == 4

    def get_marker(self):
        return "".join(self.content)

    def __str__(self):
        return self.get_marker()

    def __repr__(self):
        return f"<Marker {self} - Is Marker: {self.has_no_double()}"


def get_marker(signal: str):
    m = MarkerChecker()
    for i, c in enumerate(signal):
        if m.push(c):
            return i + 1  # because of zero indexing
    return -1


def part1():
    signal = read_input(2022, 6).strip()
    print(get_marker(signal))


if __name__ == "__main__":
    part1()
