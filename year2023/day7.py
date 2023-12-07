from utils.puzzle import Puzzle


def get_card_points(card: str):
    return "123456789TJQKA".find(sortable_to_hand(card))+1


def get_hand_points(hand: str):
    counts = []
    for i in hand:
        counts.append(hand.count(i))
    if 5 in counts:
        return 21  # 5 of a kind
    if 4 in counts:
        return 20  # 4 of a kind
    if 3 in counts and 2 in counts:
        return 19  # Full house
    if 3 in counts:  # but not 2
        return 18  # three of a kind
    if counts.count(2) == 4:
        return 17  # two pairs
    if 2 in counts:
        return 16  # on pair
    return 15

FIVE_OF_A_KIND = 21
FOUR_OF_A_KIND = 20
FULL_HOUSE = 19
THREE_OF_A_KIND = 18
TWO_PAIRS = 17
ONE_PAIR = 16
HIGH_CARD = 15

def get_hand_points_joker(hand: str):
    hand = hand.replace("0", "J")
    counts = []
    jokers = hand.count("J")
    hand = hand.replace("J","")
    for i in hand:
        counts.append(hand.count(i))
    if 5 in counts:
        return FIVE_OF_A_KIND  # 5 of a kind
    if 4 in counts:
        if jokers == 1:
            return FIVE_OF_A_KIND
        return FOUR_OF_A_KIND  # 4 of a kind
    if 3 in counts and 2 in counts:
        if jokers == 3 or jokers == 2:
            return FIVE_OF_A_KIND  # 5 of a kind
        if jokers == 1:
            return FOUR_OF_A_KIND  # four of a kind
        return FULL_HOUSE  # Full house
    if 3 in counts:  # but not 2
        # three times the same, two different
        if jokers == 2:  # should not be possible :D
            return FIVE_OF_A_KIND
        if jokers == 1:
            return FOUR_OF_A_KIND  # make a four of a kind
        return THREE_OF_A_KIND  # three of a kind
    if counts.count(2) == 4 and len(counts) != 2:
        if jokers == 1:
            return FULL_HOUSE  # full house
        return TWO_PAIRS  # two pairs
    if 2 in counts:  # one pair
        if jokers == 1:
            return THREE_OF_A_KIND  # three of a kind
        if jokers == 2:
            return FOUR_OF_A_KIND
        if jokers == 3:
            return FIVE_OF_A_KIND
        return ONE_PAIR  # one pair
    # Nothing matches, but we have a joker
    if jokers == 1:
        return ONE_PAIR
    if jokers == 2:
        return THREE_OF_A_KIND
    if jokers == 3:
        return FOUR_OF_A_KIND
    if jokers >= 4:
        return FIVE_OF_A_KIND
    # nothing matches, no joker
    return HIGH_CARD


def get_winning_hand(hand1: str, hand2: str):
    points1 = get_hand_points(hand1)
    points2 = get_hand_points(hand2)

    if points1 > points2:
        return 1  # first hand
    if points2 > points1:
        return 2  # second hand

    for i in range(len(hand1)):
        c1 = hand1[i]
        c2 = hand2[i]
        if get_card_points(c1) > get_card_points(c2):
            return 1
        if get_card_points(c2) > get_card_points(c1):
            return 2
    return 0  # draw?


def hand_to_sortable(hand: str, part2=False) -> str:
    j_replace = "0" if part2 else "W"
    return hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", j_replace).replace("T","V")


def sortable_to_hand(hand: str, part2=False) -> str:
    j_replace = "0" if part2 else "W"
    return hand.replace("Z", "A").replace("Y", "K").replace("X", "Q").replace(j_replace, "J").replace("V","T")



def rank_hands(hands_with_bets: [str], part2=False) -> [str]:
    hands_with_bets = [hand_to_sortable(i, part2) for i in hands_with_bets]
    # Sort the hands alphabetically.
    # So higher card comes first
    hands_with_bets = sorted(hands_with_bets)[::-1]

    # second, sort by points
    hands_with_points = []
    for hand in hands_with_bets:
        h, bet = hand.split(" ")
        hand_points = get_hand_points(h) if not part2 else get_hand_points_joker(h)
        hands_with_points.append((h, hand_points, bet))

    # now sort
    completely_sorted = sorted(hands_with_points, key=lambda x:-x[1])

    ret = [sortable_to_hand(i[0], part2)+" "+str(i[2]) for i in completely_sorted][::-1]
    # Use reversed list, so we have the lowest first
    return ret

def get_total_winnings(hands_with_bets: [str], part2=False) -> int:
    ranked = rank_hands(hands_with_bets, part2)
    total = 0
    for rank, hand_with_bet in enumerate(ranked):
        hand, bet = hand_with_bet.split(" ")
        total += (rank+1) * int(bet)
    return total


class PokerEvaluator(Puzzle):
    DAY = 7
    YEAR = 2023

    def part1(self):
        return get_total_winnings(self.input.split("\n"), part2=False)

    def part2(self):
        return get_total_winnings(self.input.split("\n"), part2=True)
