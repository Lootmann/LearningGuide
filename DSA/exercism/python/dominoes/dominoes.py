from itertools import permutations


def validation(chain: list) -> bool:
    for i in range(len(chain) - 1):
        if chain[i][1] != chain[i + 1][0]:
            chain[i + 1] = (chain[i + 1][1], chain[i + 1][0])

        if chain[i][1] != chain[i + 1][0]:
            return False

    return chain[-1][1] == chain[0][0]


def can_chain(dominoes: list):
    if dominoes == []:
        return []

    for chains in permutations(dominoes):
        lists = list(chains)
        if validation(lists):
            return lists

    return None
