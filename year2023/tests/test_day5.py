from year2023.day5 import SeedMap

EXAMPLE = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_get_map_parts():
    m = SeedMap(EXAMPLE)
    parts = m.get_input_parts()
    assert len(parts) == 8


def test_get_seed_list():
    m = SeedMap(EXAMPLE)
    assert m.seeds == [79, 14, 55, 13]


def test_process_map_name():
    m = SeedMap(EXAMPLE)
    assert m.maps[0]["name"] == "seed-to-soil"
    assert m.maps[1]["name"] == "soil-to-fertilizer"
    assert m.maps[2]["name"] == "fertilizer-to-water"
    assert m.maps[3]["name"] == "water-to-light"
    assert m.maps[4]["name"] == "light-to-temperature"
    assert m.maps[5]["name"] == "temperature-to-humidity"
    assert m.maps[6]["name"] == "humidity-to-location"
    assert len(m.maps) == 7


def test_get_location():
    m = SeedMap(EXAMPLE)
    seed_to_soil = m.maps[0]
    assert seed_to_soil["name"] == "seed-to-soil"
    assert m.get_location(96, 0) == 98


def test_get_soil_numbers():
    m = SeedMap(EXAMPLE)
    out = []
    for seed in m.seeds:
        out.append(m.get_location(seed, 0))
    assert out == [81, 14, 57, 13]


def test_get_end_position_single():
    m = SeedMap(EXAMPLE)
    assert m.get_end_position(79) == 82


def test_get_all_end_positions():
    m = SeedMap(EXAMPLE)
    all_positions = m.get_all_end_positions()
    assert all_positions == [82, 43, 86, 35]


def test_get_lowest_location():
    m = SeedMap(EXAMPLE)
    lowest = m.get_lowest_position()
    assert lowest == 35


def test_get_seed_ranges():
    m = SeedMap(EXAMPLE)
    ranges = m.seed_ranges
    assert len(ranges) == 2
    range1, range2 = ranges
    assert range1.start == 79
    assert range1.stop == 79 + 14
    assert range2.start == 55
    assert range2.stop == 55 + 13


def test_lowest_part_2():
    m = SeedMap(EXAMPLE)
    r = m.get_lowest_part2_position()
    assert r == 46
