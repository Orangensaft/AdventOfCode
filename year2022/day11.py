import math
from utils.puzzle import Puzzle


class Monkey:
    def __init__(self):
        self.index = -1
        self.items = []
        self.op = lambda old: old
        self.mod = -1
        self.true_target = -1
        self.false_target = -1
        self.inspections = 0
        self.get_bored = True
        self.common_multiple = 1

    @staticmethod
    def from_data(data: [str]):
        m = Monkey()
        m.index = int(data[0].split(" ")[-1].split(":")[0])
        items = data[1].split(": ")[-1].split(", ")
        m.items = [int(i) for i in items]
        op = data[2].split(" = ")[-1]
        m.op = lambda old: eval(op)  # 🤷
        mod = data[3].split(" by ")[-1]
        m.mod = int(mod)
        m.true_target = int(data[4].split("monkey ")[-1])
        m.false_target = int(data[5].split("monkey ")[-1])
        return m

    def get_target(self, item):
        if item % self.mod == 0:
            return self.true_target
        else:
            return self.false_target

    def increase_worry(self, item):
        return self.op(item)

    def bore_item(self, item):
        return math.floor(item / 3)

    def inspect_next(self):
        self.inspections += 1
        item = self.items.pop(0)
        # first inspect the item
        item = self.increase_worry(item)
        # get bored by item
        if self.get_bored:
            item = self.bore_item(item)
        else:
            item = item % self.common_multiple
        target = self.get_target(item)
        return item, target

    def catch(self, item):
        self.items.append(item)

    def has_items(self):
        return len(self.items) > 0


class MonkeySimulator:
    def __init__(self, data: str, get_bored=True):
        self.common_multiple = 1  # to cap worry level but not mess with the mod checks
        monkey_data = data.split("\n\n")
        monkeys = {}
        for d in monkey_data:
            monkey = Monkey.from_data(d.split("\n"))
            monkey.get_bored = get_bored
            monkeys[monkey.index] = monkey
            self.common_multiple *= monkey.mod
        for _, monkey in monkeys.items():
            monkey.common_multiple = self.common_multiple
        self.monkeys = monkeys

    def single_round(self):
        for _, monkey in self.monkeys.items():
            while monkey.has_items():
                item, target = monkey.inspect_next()
                self.monkeys[target].catch(item)

    def full_simulation(self, rounds=20):
        for i in range(rounds):
            self.single_round()

    def get_monkey_business(self):
        inspects = sorted([m.inspections for _, m in self.monkeys.items()])[::-1]
        top, second = inspects[:2]
        return top * second


class Day11(Puzzle):
    YEAR = 2022
    DAY = 11

    def part1(self):
        sim = MonkeySimulator(self.input)
        sim.full_simulation()
        return sim.get_monkey_business()

    def part2(self):
        sim = MonkeySimulator(self.input, get_bored=False)
        sim.full_simulation(10000)
        return sim.get_monkey_business()
