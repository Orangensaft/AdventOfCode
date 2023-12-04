from utils.puzzle import Puzzle


class Card:
    def __init__(self, line: str):
        self.winners = []
        self.numbers = []
        win, num = line.split(" | ")
        win = win.split(":")[-1].strip().replace("  ", " ")
        num = num.strip().replace("  ", " ")
        self.winners = [int(i) for i in win.split(" ")]
        self.numbers = [int(i) for i in num.split(" ")]

    def get_my_winning_numbers(self) -> [int]:
        return [i for i in self.numbers if i in self.winners]

    def get_points(self) -> int:
        wins = self.get_my_winning_numbers()
        if not len(wins):
            return 0
        return 2 ** (len(wins) - 1)


def parse_cards(input_str) -> [Card]:
    cards = []
    for line in input_str.split("\n"):
        card = Card(line)
        cards.append(card)
    return cards


def process_card_wins(cards: [Card]):
    # number of cards, card 1 is at index 0
    card_counts = [1 for i in range(len(cards))]
    for i, card in enumerate(cards):
        count = card_counts[i]
        wins = len(card.get_my_winning_numbers())
        # increment card counts
        if wins == 0:
            continue  # no incrementing to be done
        # increment the next (wins) card counts
        for j in range(i + 1, i + wins + 1):
            if j >= len(card_counts):
                # don't go over end of the list
                break
            card_counts[j] += count
    return card_counts


class CardScratcher3000(Puzzle):
    DAY = 4
    YEAR = 2023

    def part1(self):
        cards = parse_cards(self.input)
        return sum([c.get_points() for c in cards])

    def part2(self):
        cards = parse_cards(self.input)
        counts = process_card_wins(cards)
        # from matplotlib import pyplot as plt

        # plt.plot(counts)
        # plt.show()
        return sum(counts)
