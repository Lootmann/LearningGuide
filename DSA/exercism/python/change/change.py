import collections
from typing import List


def find_fewest_coins(coins: List[int], target: int) -> List[int]:
    """find_fewest_coins

    :param coins: List
    :param target: int
    :return: List
    """
    coins.sort()

    if target == 0:
        return []

    if target < 0:
        raise ValueError("target can't be negative")

    if coins[0] > target:
        raise ValueError("can't make target with given coins")

    value_to_coins = {0: []}
    queue = collections.deque()
    queue.append(0)

    while queue:
        value = queue.popleft()

        if value == target:
            return value_to_coins[value]

        for coin in coins:
            next_value = value + coin
            if next_value <= target and next_value not in value_to_coins:
                next_coins = value_to_coins[value][:]
                next_coins.append(coin)

                value_to_coins[next_value] = next_coins
                queue.append(next_value)

    raise ValueError("can't make target with given coins")
