from year2023.day7 import get_card_points, get_hand_points, get_winning_hand, rank_hands, get_total_winnings, \
    get_hand_points_joker, HIGH_CARD, FULL_HOUSE, THREE_OF_A_KIND, FIVE_OF_A_KIND, FOUR_OF_A_KIND

EXAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n")


EXAMPLE_TWO = """2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41""".split("\n")

def test_get_card_points():
    assert get_card_points("1") == 1
    assert get_card_points("A") == 14


def test_get_hand_points():
    assert get_hand_points("12345") == 15
    assert get_hand_points("12344") == 16
    assert get_hand_points("12233") == 17
    assert get_hand_points("12333") == 18
    assert get_hand_points("11222") == 19
    assert get_hand_points("41444") == 20
    assert get_hand_points("55555") == 21


def test_get_winning_hand():
    assert get_winning_hand("33332", "2AAAA") == 1
    assert get_winning_hand("77788", "77888") == 2


def test_sort_hands():
    sorted_hands = rank_hands(EXAMPLE)
    assert sorted_hands == ["32T3K 765", "KTJJT 220", "KK677 28", "T55J5 684", "QQQJA 483"]


def test_get_total_winnings():
    assert get_total_winnings(EXAMPLE) == 6440



def test_rankit_two():
    # example from reddit
    # https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
    assert get_total_winnings(EXAMPLE_TWO) == 6592


def test_hand_with_jokers():
    assert get_hand_points_joker("12345") == HIGH_CARD
    assert get_hand_points_joker("2233J") == FULL_HOUSE
    assert get_hand_points_joker("AJJ94") == THREE_OF_A_KIND
    assert get_hand_points_joker("AAJ55") == FULL_HOUSE
    assert get_hand_points_joker("JJJJ1") == FIVE_OF_A_KIND
    assert get_hand_points_joker("JJJ22") == FIVE_OF_A_KIND
    assert get_hand_points_joker("JJ222") == FIVE_OF_A_KIND
    assert get_hand_points_joker("J2222") == FIVE_OF_A_KIND
    assert get_hand_points_joker("T55J5") == FOUR_OF_A_KIND
    assert get_hand_points_joker("KTJJT") == FOUR_OF_A_KIND
    assert get_hand_points_joker("QQQJA") == FOUR_OF_A_KIND


def test_get_winnings_part2_example():
    assert get_total_winnings(EXAMPLE, part2=True) == 5905