from utils.puzzle import Puzzle

class Present:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    @staticmethod
    def from_line(s: str):
        l, w, h = [int(i) for i in s.split("x")]
        return Present(l, w, h)

    def get_wrapping_area(self):
        sides = [2*self.l*self.w,2*self.w*self.h,2*self.h*self.l]
        return sum(sides) + min([s//2 for s in sides])

    def get_band_size(self):
        side1, side2 = sorted([self.l, self.w, self.h])[:2]
        band = 2*side1+2*side2
        ribbon = self.l * self.w * self.h
        return band + ribbon

class Day2(Puzzle):
    YEAR = 2015
    DAY = 2

    def part1(self):
        area = 0
        for line in self.input.split("\n"):
            area += Present.from_line(line).get_wrapping_area()
        return area

    def part2(self):
        ...

