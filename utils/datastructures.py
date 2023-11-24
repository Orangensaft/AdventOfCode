class Field2D:

    def __init__(self, size_x, size_y, default=None):
        self.size_x = size_x
        self.size_y = size_y
        self.field = [default for _ in range(size_x * size_y)]

    def __get_idx(self, x, y):
        return y * self.size_x + x

    def get_surrounding_coords(self, x, y, diag=True):
        out = set()
        for _x in range(-1, 2):
            for _y in range(-1, 2):
                if not diag and not (_x == 0 or _y == 0):
                    continue

                if x + _x < 0:
                    continue
                if y + _y < 0:
                    continue
                if x + _x > self.size_x - 1:
                    continue
                if y + _y > self.size_y - 1:
                    continue
                out.add((x + _x, y + _y))
        out.remove((x, y))
        return list(out)

    def count(self, item):
        return sum([1 for i in self.field if i == item])

    def __getitem__(self, coord):
        return self.field[self.__get_idx(*coord)]

    def __setitem__(self, coord, value):
        self.field[self.__get_idx(*coord)] = value

    def __str__(self):
        out = ""
        for y in range(self.size_y):
            for x in range(self.size_x):
                out += str(self[x, y])
            out += "\n"
        return out
