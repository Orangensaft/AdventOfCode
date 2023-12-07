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


def hand_to_sortable(hand: str) -> str:
    return hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "W").replace("T","V")


def sortable_to_hand(hand: str) -> str:
    return hand.replace("Z", "A").replace("Y", "K").replace("X", "Q").replace("W", "J").replace("V","T")



def rank_hands(hands_with_bets: [str]) -> [str]:
    hands_with_bets = [hand_to_sortable(i) for i in hands_with_bets]
    # Sort the hands alphabetically.
    # So higher card comes first
    hands_with_bets = sorted(hands_with_bets)[::-1]

    # second, sort by points
    hands_with_points = []
    for hand in hands_with_bets:
        h, bet = hand.split(" ")
        hands_with_points.append((h, get_hand_points(h), bet))

    # now sort
    completely_sorted = sorted(hands_with_points, key=lambda x:-x[1])

    ret = [sortable_to_hand(i[0])+" "+str(i[2]) for i in completely_sorted][::-1]
    # Use reversed list, so we have the lowest first
    return ret

def get_total_winnings(hands_with_bets: [str]) -> int:
    ranked = rank_hands(hands_with_bets)
    total = 0
    for rank, hand_with_bet in enumerate(ranked):
        hand, bet = hand_with_bet.split(" ")
        total += (rank+1) * int(bet)
    return total


class PokerEvaluator(Puzzle):
    DAY = 7
    YEAR = 2023

    def part1(self):
        return get_total_winnings(self.input.split("\n"))
