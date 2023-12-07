from year2023.day7 import get_card_points, get_hand_points, get_winning_hand, rank_hands, get_total_winnings

EXAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n")

def test_get_card_points():
    assert get_card_points("1") == 1
    assert get_card_points("A") == 14


def test_get_hand_points():
    assert get_hand_points("12345") == 5
    assert get_hand_points("12344") == 15
    assert get_hand_points("12233") == 16
    assert get_hand_points("12333") == 17
    assert get_hand_points("11222") == 18
    assert get_hand_points("41444") == 19
    assert get_hand_points("55555") == 20


def test_get_winning_hand():
    assert get_winning_hand("33332", "2AAAA") == 1
    assert get_winning_hand("77788", "77888") == 2


def test_sort_hands():
    sorted_hands = rank_hands(EXAMPLE)
    assert sorted_hands == ["32T3K 765", "KTJJT 220", "KK677 28", "T55J5 684", "QQQJA 483"]


def test_get_total_winnings():
    assert get_total_winnings(EXAMPLE) == 6440

