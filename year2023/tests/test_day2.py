from year2023.day2 import Round, Game, FullGame

EXAMPLE = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_parsing_round():
    r = Round.from_game_str("8 green, 6 blue, 20 red")
    assert r.red == 20
    assert r.green == 8
    assert r.blue == 6


def test_parsing_sparse_round():
    r = Round.from_game_str("12 green")
    assert r.green == 12
    assert r.blue == 0
    assert r.red == 0


def test_parse_game_id():
    g = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert g.game_id == 1


def test_parse_game_rounds():
    g = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert len(g.rounds) == 3


def test_parse_game_details():
    g = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    r1 = g.rounds[0]
    assert r1.blue == 3
    assert r1.red == 4
    assert r1.green == 0


def test_input_parsing():
    full_game = FullGame(EXAMPLE)
    assert len(full_game.games) == 5


def test_input_example_part_1():
    full_game = FullGame(EXAMPLE)
    possible_ids = full_game.get_possible_game_ids(12, 13, 14)
    assert possible_ids == [1, 2, 5]


def test_power_example_1():
    g = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert g.get_power() == 48


def test_power_sum():
    f = FullGame(EXAMPLE)
    assert f.get_power_sum() == 2286
