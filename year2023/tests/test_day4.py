from year2023.day4 import parse_cards, process_card_wins

EXAMPLE = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def test_parse_cards():
    cards = parse_cards(EXAMPLE)
    assert len(cards) == 6
    for card in cards:
        assert len(card.winners) == 5
        assert len(card.numbers) == 8


def test_card_number_ordering():
    cards = parse_cards(EXAMPLE)
    card = cards[0]
    assert card.winners == [41, 48, 83, 86, 17]
    assert card.numbers == [83, 86, 6, 31, 17, 9, 48, 53]


def test_get_winners():
    cards = parse_cards(EXAMPLE)
    card = cards[0]
    assert set(card.get_my_winning_numbers()) == {48, 83, 17, 86}


def test_get_winner_points():
    cards = parse_cards(EXAMPLE)
    card = cards[0]
    assert card.get_points() == 8


def test_all_points():
    cards = parse_cards(EXAMPLE)
    all_points = [c.get_points() for c in cards]
    assert all_points == [8, 2, 2, 1, 0, 0]


def test_total_points():
    cards = parse_cards(EXAMPLE)
    assert sum([c.get_points() for c in cards]) == 13


def test_parse_card_counts():
    cards = parse_cards(EXAMPLE)
    counts = process_card_wins(cards)
    assert counts == [1, 2, 4, 8, 14, 1]


def test_parse_card_total():
    cards = parse_cards(EXAMPLE)
    counts = process_card_wins(cards)
    assert sum(counts) == 30
