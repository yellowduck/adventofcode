"""
--- Day 7: Camel Cards ---

https://adventofcode.com/2023/day/7

https://docs.python.org/3/howto/sorting.html#sortinghowto
"""
from collections import defaultdict
from functools import cmp_to_key

def problem(part=1, test=None):
    if test is None:
        data = open("day7.input", "rt").readlines()
    else:
        data = test.split("\n")

    hands = {}
    for line in data:
        hand,value = line.strip().split(" ")
        hands[hand] = int(value)

    def card_type(hand):
        """Every hand is exactly one type. From strongest to weakest, they are:

        7. Five of a kind, where all five cards have the same label: AAAAA
        6. Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        5. Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        4. Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        3. Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        2. One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        1. High card, where all cards' labels are distinct: 23456
        """
        count = defaultdict(int)
        for card in hand:
            count[card] +=1
        counts = count.values()
        # 7. Five of a kind
        if len(count)==1:
            return 7
        # 6. Four of a kind
        elif 4 in counts:
            return 6
        # 1. High card
        elif len(count)==5:
            return 1
        # 5. Full house
        elif len(count)==2 and 3 in counts:
            return 5
        # 4. Three of a kind
        elif len(count)==3 and 3 in counts:
            return 4
        # 3. Two pair
        elif len(count)==3 and 2 in counts:
            return 3
        # 2. One pair
        elif len(count)==4:
            return 2
        else:
            assert False, "invalid hand"

    def sort_hands(a, b):
        """ Custom sort method.

        1. sort on type
        2. then card order
        """
        compare = card_type(a) - card_type(b)
        if compare != 0:
            return compare

        rankings = "AKQJT98765432"[::-1]
        for ca, cb in zip(a,b):
            if ca==cb:
                continue
            else:
                return rankings.index(ca)-rankings.index(cb)
        return 0

    # 32T3K, KTJJT, KK677, T55J5, QQQJA
    # sorted_hands = sorted(hands)
    ranking = sorted(hands.keys(), key=cmp_to_key(sort_hands))

    result = sum(hands[hand]*i for i,hand in enumerate(ranking,1))

    return result

if __name__ == '__main__':

    test="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

    exp = 6440
    result = problem(part=1, test=test)
    assert exp==result, f"Part 1: received={result} {exp=}"

    exp = 251806792
    result = problem(part=1)
    print(f"Part 1: {result}")
    assert exp==result, f"Part 1: received={result} {exp=}"

    exp = 71503
    result = problem(part=2, test=test)
    assert exp==result, f"Part 2: received={result} {exp=}"

    exp = 46173809
    result = problem(part=2)
    print(f"Part 2: {result}")
    assert exp==result, f"Part 2: received={result} {exp=}"
