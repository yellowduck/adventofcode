"""
--- Day 4: Scratchcards ---

https://adventofcode.com/2023/day/4
"""
def problem(part=1, test=False):
    if not test:
        data = open("day4.input", "rt").readlines()
    else:
        data = test.split("\n")

    sum_of_points = 0
    cardCount = [0] * len(data)

    for card, line in enumerate(data):
        _, numbers = line.strip().split(": ")
        numbers = numbers.split(" | ")
        lists = [n.strip().replace("  "," ").split(" ") for n in numbers]
        sets = [{int(n) for n in l} for l in lists]
        match = len(sets[0] & sets[1])
        # part I
        if match > 0:
            sum_of_points += pow(2, match-1)

        # part II
        cardCount[card] += 1
        for c in range(card+1, card+match+1):
            cardCount[c] += cardCount[card]

    return sum_of_points, sum(cardCount)

if __name__ == '__main__':

    test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    points,cards = problem(part=1, test=test)
    exp_points = 13
    exp_cards = 30
    assert exp_points==points, f"received={points} {exp_points=}"
    assert exp_cards==cards, f"received={points} {exp_cards=}"

    exp_points = 20667
    exp_cards = 5833065
    points, cards = problem()
    print(f"Part 1: {points}")
    print(f"Part 2: {cards}")
    assert exp_points==points, f"received={points} {exp_points=}"
    assert exp_cards==cards, f"received={points} {exp_cards=}"