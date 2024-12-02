from year2022.day11 import Monkey, MonkeySimulator

FULL_DATA = """Monkey 0:
      Starting items: 79, 98
      Operation: new = old * 19
      Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3

    Monkey 1:
      Starting items: 54, 65, 75, 74
      Operation: new = old + 6
      Test: divisible by 19
        If true: throw to monkey 2
        If false: throw to monkey 0

    Monkey 2:
      Starting items: 79, 60, 97
      Operation: new = old * old
      Test: divisible by 13
        If true: throw to monkey 1
        If false: throw to monkey 3

    Monkey 3:
      Starting items: 74
      Operation: new = old + 3
      Test: divisible by 17
        If true: throw to monkey 0
        If false: throw to monkey 1
    """


def test_parse_monkey():
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3"""
    m = Monkey.from_data(data.split("\n"))
    assert m.index == 0
    assert m.items == [79, 98]
    assert m.op(2) == 38
    assert m.mod == 23
    assert m.true_target == 2
    assert m.false_target == 3


def test_parse_one_item():
    data = """Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    m = Monkey.from_data(data.split("\n"))
    assert m.items == [74]
    assert m.op(10) == 13


def test_get_target_non_div():
    m = Monkey()
    m.mod = 5
    m.true_target = 5
    m.false_target = 10
    assert m.get_target(1) == 10


def test_get_target_div():
    m = Monkey()
    m.mod = 5
    m.true_target = 5
    m.false_target = 10
    assert m.get_target(25) == 5


def test_increase_worry_level():
    m = Monkey()
    m.op = lambda old: old + 1
    assert m.increase_worry(1) == 2


def test_get_bored():
    m = Monkey()
    assert m.bore_item(3) == 1


def test_get_bored_non_div_three():
    m = Monkey()
    assert m.bore_item(5) == 1


def test_inspect():
    m = Monkey.from_data(
        """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3""".split("\n")
    )
    item, target = m.inspect_next()
    assert item == 500
    assert target == 3


def test_full_parse():
    s = MonkeySimulator(FULL_DATA)
    assert s.monkeys[0].items == [79, 98]
    assert s.monkeys[0].mod == 23
    assert s.monkeys[0].op(1) == 19
    assert s.monkeys[2].items == [79, 60, 97]
    assert s.monkeys[2].op(2) == 4


def test_single_round():
    sim = MonkeySimulator(FULL_DATA)
    sim.single_round()
    assert not sim.monkeys[2].has_items()
    assert not sim.monkeys[3].has_items()
    for i in range(19):
        sim.single_round()
    assert sim.monkeys[0].items == [10, 12, 14, 26, 34]
    assert sim.monkeys[1].items == [245, 93, 53, 199, 115]
    assert sim.monkeys[2].items == []
    assert sim.monkeys[3].items == []


def test_full_simulation():
    sim = MonkeySimulator(FULL_DATA)
    sim.full_simulation()
    assert sim.monkeys[0].inspections == 101
    assert sim.monkeys[1].inspections == 95
    assert sim.monkeys[2].inspections == 7
    assert sim.monkeys[3].inspections == 105


def test_get_monkey_business():
    sim = MonkeySimulator(FULL_DATA)
    sim.full_simulation()
    assert sim.get_monkey_business() == 10605
