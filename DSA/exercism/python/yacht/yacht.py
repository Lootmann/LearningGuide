# Score categories.
# Change the values as you see fit.
from collections import defaultdict
from typing import List

YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 10
FOUR_OF_A_KIND = 15
LITTLE_STRAIGHT = 25
BIG_STRAIGHT = 35
CHOICE = -1


def score(dice: List[int], category: int) -> int:
    d = defaultdict(int)

    # choice - special case
    if category == CHOICE:
        return sum(dice)

    for num in dice:
        d[num] += 1

    # check one
    if 1 in d and category == ONES:
        return 1 * d[1]

    if 2 in d and category == TWOS:
        return 2 * d[2]

    if 3 in d and category == THREES:
        return 3 * d[3]

    if 4 in d and category == FOURS:
        return 4 * d[4]

    if 5 in d and category == FIVES:
        return 5 * d[5]

    if 6 in d and category == SIXES:
        return 6 * d[6]

    for k, v in d.items():
        # Yacht
        if v == 5 and category == YACHT:
            return 50

        # Four of a Kind
        if v >= 4 and category == FOUR_OF_A_KIND:
            return 4 * k

    # little straight
    if set([1, 2, 3, 4, 5]) == set(d) and category == LITTLE_STRAIGHT:
        return 30

    # big straight
    if set([2, 3, 4, 5, 6]) == set(d) and category == BIG_STRAIGHT:
        return 30

    # full house
    if 2 in d.values() and 3 in d.values() and category == FULL_HOUSE:
        total = 0
        for k, v in d.items():
            if v == 2:
                total += 2 * k
            if v == 3:
                total += 3 * k
        return total

    return 0
