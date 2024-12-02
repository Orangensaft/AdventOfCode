from year2022.day10 import CRT

EXAMPLE_SMALL_PART_1 = """noop
addx 3
addx -5""".split("\n")

EXAMPLE_BIG_PART_1 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".split("\n")


def test_init_value():
    r = CRT()
    assert r.X == 1


def test_addx_value():
    r = CRT()
    r.addx(5)
    assert r.X == 6


def test_addx_neg():
    r = CRT()
    r.addx(-5)
    assert r.X == -4


def test_get_signal_at_clk_noop():
    r = CRT()
    r.noop()
    assert r.get_signal_after(1) == 1
    assert r.get_signal_after(12) == 1


def test_get_signal_at_clk_addx():
    r = CRT()
    r.addx(5)
    assert r.get_signal_after(1) == 1
    assert r.get_signal_after(2) == 6


def test_mini_example_after():
    r = CRT()
    r.commands(EXAMPLE_SMALL_PART_1)
    assert r.get_signal_after(1) == 1
    assert r.get_signal_after(2) == 1
    assert r.get_signal_after(3) == 4
    assert r.get_signal_after(4) == 4
    assert r.get_signal_after(5) == -1


def test_mini_example_during():
    r = CRT()
    r.commands(EXAMPLE_SMALL_PART_1)
    assert r.get_signal_during(1) == 1
    assert r.get_signal_during(2) == 1
    assert r.get_signal_during(3) == 1
    assert r.get_signal_during(4) == 4
    assert r.get_signal_during(5) == 4


def test_huge_example():
    r = CRT()
    r.commands(EXAMPLE_BIG_PART_1)
    assert r.get_signal_during(20) == 21
    assert r.get_signal_strength(20) == 420
    assert r.get_signal_strength(60) == 1140
    assert r.get_signal_strength(100) == 1800
    assert r.get_signal_strength(140) == 2940
    assert r.get_signal_strength(180) == 2880
    assert r.get_signal_strength(220) == 3960


def test_hug_example_sum():
    ret = CRT().commands(EXAMPLE_BIG_PART_1).get_sum_strengths()
    assert ret == 13140


def test_huge_example_pixel():
    r = CRT().commands(EXAMPLE_BIG_PART_1)
    assert r.get_pixel_value(0) == "#"
    assert r.get_pixel_value(1) == "#"
    assert r.get_pixel_value(2) == "."


def test_full_huge_example_pixel():
    r = CRT().commands(EXAMPLE_BIG_PART_1)
    out = r.get_screen()
    assert (
        out
        == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    )
