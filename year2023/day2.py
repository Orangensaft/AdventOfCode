from utils.puzzle import Puzzle


class Round:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def is_possible(self, max_r: int, max_g: int, max_b: int):
        return max_r >= self.red and max_g >= self.green and max_b >= self.blue

    @staticmethod
    def from_game_str(s: str) -> "Round":
        r = Round(0, 0, 0)
        counts = s.split(", ")
        for i in counts:
            amount, color = i.split(" ")
            if color == "red":
                r.red = int(amount)
            if color == "blue":
                r.blue = int(amount)
            if color == "green":
                r.green = int(amount)
        return r


class Game:
    def __init__(self, game_line: str):
        game_desc, rounds = game_line.split(": ")
        self.game_id: int = int(game_desc.split(" ")[-1])
        rounds = rounds.split("; ")
        self.rounds = []
        for round_str in rounds:
            self.rounds.append(Round.from_game_str(round_str))

    def is_possible(self, max_r: int, max_g: int, max_b: int):
        return all([r.is_possible(max_r, max_g, max_b) for r in self.rounds])

    def get_power(self):
        min_r = max([r.red for r in self.rounds])
        min_b = max([r.blue for r in self.rounds])
        min_g = max([r.green for r in self.rounds])
        return min_r * min_b * min_g


class FullGame:
    def __init__(self, input_str: str):
        self.games = []
        for line in input_str.split("\n"):
            game = Game(line)
            self.games.append(game)

    def get_possible_game_ids(self, max_r: int, max_g: int, max_b: int):
        possible = []
        for game in self.games:
            if game.is_possible(max_r, max_g, max_b):
                possible.append(game.game_id)
        return possible

    def get_power_sum(self):
        # hope it's over 9000
        return sum([g.get_power() for g in self.games])


class DiceShredder5000(Puzzle):
    DAY = 2
    YEAR = 2023

    def part1(self):
        full_game = FullGame(self.input)
        ids = full_game.get_possible_game_ids(12, 13, 14)
        return sum(ids)

    def part2(self):
        full_game = FullGame(self.input)
        return full_game.get_power_sum()
