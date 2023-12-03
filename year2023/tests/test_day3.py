from year2023.day3 import parse_input

EXAMPLE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_day3_parsing():
    field = parse_input(EXAMPLE)
    assert field.size_y == 10
    assert field.size_x == 10


def test_day3_coords():
    field = parse_input(EXAMPLE)
    assert field[0, 0] == "4"
    assert field[9, 9] == "."
    assert field[3, 1] == "*"


def test_surrounding_items():
    field = parse_input(EXAMPLE)
    items = field.get_surrounding_items(0, 0, diag=True)
    assert len(items) == 3
    assert "6" in items
    assert items.count(".") == 2


def test_symbol_adjacent():
    field = parse_input(EXAMPLE)
    assert field.symbol_adjacent(2, 0)


def test_get_part_numbers():
    field = parse_input(EXAMPLE)
    parts, _ = field.get_part_numbers()
    assert parts == ["467", "35", "633", "617", "592", "755", "664", "598"]


def test_get_non_parts():
    field = parse_input(EXAMPLE)
    _, not_parts = field.get_part_numbers()
    assert not_parts == ["114", "58"]


def test_full_example():
    field = parse_input(EXAMPLE)
    parts, _ = field.get_part_numbers()
    assert sum(int(i) for i in parts) == 4361


def test_get_number_start_end():
    field = parse_input(EXAMPLE)
    start = field.get_number_start(7, 0)
    assert start == 5


def test_get_number_start_middle():
    field = parse_input(EXAMPLE)
    start = field.get_number_start(6, 0)
    assert start == 5


def test_get_number_start_start():
    field = parse_input(EXAMPLE)
    start = field.get_number_start(5, 0)
    assert start == 5


def test_get_number_start_left():
    field = parse_input(EXAMPLE)
    assert field.get_number_start(0, 0) == 0


def test_get_number_start_left_plus_one():
    field = parse_input(EXAMPLE)
    assert field.get_number_start(1, 0) == 0


def test_get_number_start_left_plus_two():
    field = parse_input(EXAMPLE)
    assert field.get_number_start(2, 0) == 0


def test_get_number():
    field = parse_input(EXAMPLE)
    num = field.get_full_number(2, 0)
    assert num == "467"


def test_get_two():
    field = parse_input(EXAMPLE)
    num = field.get_full_number(6, 0)
    assert num == "114"


def test_get_gears():
    field = parse_input(EXAMPLE)
    gears = field.get_gears()
    assert len(gears) == 2
    gear_nums_1 = gears[0][1]
    assert len(gear_nums_1) == 2
    assert "467" in gear_nums_1
    assert "35" in gear_nums_1

    gear_nums_2 = gears[1][1]
    assert "598" in gear_nums_2
    assert "755" in gear_nums_2


def test_get_ratios():
    field = parse_input(EXAMPLE)
    ratios = field.get_gear_ratios()
    assert ratios == [16345, 451490]


def test_example_part2():
    field = parse_input(EXAMPLE)
    total = field.get_total_gear_ratio()
    assert total == 467835
