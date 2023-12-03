from utils.datastructures import Field2D
from utils.puzzle import Puzzle


class Schematic(Field2D):
    def symbol_adjacent(self, x, y):
        surrounding = self.get_surrounding_items(x, y, diag=True)
        for i in surrounding:
            if i == ".":
                continue
            if str(i).isnumeric():
                continue
            return True

    def get_part_numbers(self):
        numbers = []
        not_parts = []
        for y in range(self.size_y):
            current_number = ""
            is_part_number = False
            for x in range(self.size_x):
                content = str(self[x, y])
                if not content.isnumeric():
                    if current_number != "":
                        if is_part_number:
                            # we are at the end of a number
                            # its a part number
                            numbers.append(current_number)
                        else:
                            not_parts.append(current_number)
                    # Reset current_number and is_part_number_flag
                    current_number = ""
                    is_part_number = False
                    continue
                current_number += content
                if self.symbol_adjacent(x, y):
                    is_part_number = True
            # End of the current row. Check if current_number is set
            if current_number != "":
                if is_part_number:
                    numbers.append(current_number)
                else:
                    not_parts.append(current_number)
        return numbers, not_parts

    def get_number_start(self, x, y):
        # get x coord where number starts
        if x == 0:
            return 0

        start = x
        cur_x = x
        while cur_x >= 0:
            if not str(self[cur_x, y]).isnumeric():
                start = cur_x + 1
                break
            cur_x -= 1
        if cur_x < 0:
            return 0
        return start

    def get_full_number(self, x, y):
        # Starting from a coord, the the full number
        # scan left, scan right
        number_start = self.get_number_start(x, y)
        current = ""
        for xi in range(number_start, self.size_x):
            c = str(self[xi, y])
            if not c.isnumeric():
                if current != "":
                    return current
            current += c
        if current != "":
            return current

    def get_surrounding_numbers(self, x, y):
        around = self.get_surrounding_coords(x, y, True)
        coords_with_nums = []
        for xi, yi in around:
            if str(self[xi, yi]).isnumeric():
                coords_with_nums.append((xi, yi))
        nums = []
        for xi, yi in coords_with_nums:
            number = self.get_full_number(xi, yi)
            nums.append(number)
        return nums

    def get_gears(self):
        gears = []
        for y in range(self.size_y):
            for x in range(self.size_x):
                content = self[x, y]
                if content != "*":
                    continue
                around = self.get_surrounding_numbers(x, y)
                # Under the assumption that a gear may NEVER connect
                # two of the same numbers
                around = set(around)
                if len(around) == 2:
                    gears.append(((x, y), list(around)))
        return gears

    def get_gear_ratios(self):
        gears = self.get_gears()
        ratios = []
        for coord, gear_nums in gears:
            ratios.append(int(gear_nums[0]) * int(gear_nums[1]))
        return ratios

    def get_total_gear_ratio(self):
        return sum(self.get_gear_ratios())


def parse_input(puzzle_input: str) -> Schematic:
    lines = puzzle_input.split("\n")
    size_x = len(lines[0])
    size_y = len(lines[1])
    f = Schematic(size_x, size_y, default=".")
    for y in range(size_x):
        for x in range(size_y):
            content = lines[y][x]
            f[x, y] = content
    return f


class SchematicParser(Puzzle):
    YEAR = 2023
    DAY = 3

    def part1(self):
        schematic = parse_input(self.input)
        parts, nonparts = schematic.get_part_numbers()
        total = sum([int(i) for i in parts])

        return total

    def part2(self):
        schematic = parse_input(self.input)
        total = schematic.get_total_gear_ratio()
        return total
