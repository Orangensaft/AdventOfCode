from utils.puzzle import Puzzle


class CRT:

    RELEVANT_CLOCKS = [20, 60, 100, 140, 180, 220]

    def __init__(self):
        self.X = 1
        self.clock = 1
        self.signals = {}

    def commands(self, cmds: list[str]):
        for cmd in cmds:
            cmd = cmd.strip()
            if cmd == "noop":
                self.noop()
            elif cmd.startswith("addx"):
                val = int(cmd.split(" ")[-1])
                self.addx(val)
        return self

    def addx(self, n):
        self.tick()
        self.X += n
        self.tick()

    def noop(self):
        self.tick()

    def tick(self):
        self.signals[self.clock] = self.X
        self.clock += 1

    def get_signal_after(self, clk):
        if clk <= 1:
            return 1
        if clk in self.signals:
            return self.signals[clk]
        else:
            return self.get_signal_after(clk - 1)

    def get_signal_during(self, clk):
        return self.get_signal_after(clk - 1)

    def get_signal_strength(self, clk):
        return self.get_signal_during(clk) * clk

    def get_sum_strengths(self):
        return sum([self.get_signal_strength(i) for i in self.RELEVANT_CLOCKS])

    def get_pixel_value(self, pos):
        # where pos = clk
        # pixel on pos p is # IF during clk p+1 value of X is between p-1 and p+2
        val = self.get_signal_during(pos + 1)
        if (pos % 40) - 1 <= val <= (pos % 40) + 1:
            return "#"
        else:
            return "."

    def get_screen(self):
        out = ""
        for i in range(240):
            if i % 40 == 0:
                out += "\n"
            out += self.get_pixel_value(i)
        return out.strip()


class Day10(Puzzle):
    YEAR = 2022
    DAY = 10

    def part1(self):
        return CRT().commands(self.input.split("\n")).get_sum_strengths()

    def part2(self):
        #print("------------------")
        #print(CRT().commands(self.input.split("\n")).get_screen())
        #print("------------------")
        return "RZHFGJCB"
