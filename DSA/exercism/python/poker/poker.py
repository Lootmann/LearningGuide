def best_hands(hands):
    hands_tup = [tup_conversion(hand) for hand in hands]
    result_list = [get_result(hand_tup) for hand_tup in hands_tup]
    max_indices = [i for i, rank in enumerate(result_list) if rank == max(result_list)]
    return [hands[index] for index in max_indices]


def tup_conversion(hand):
    card_list = hand.split(" ")
    tup_list = [(card[:-1], card[-1]) for card in card_list]
    return tup_list


def get_result(hand_tup):
    suits = [suit for _, suit in hand_tup]
    ranks = sorted(
        [
            int(
                rank.replace("J", "11")
                .replace("Q", "12")
                .replace("K", "13")
                .replace("A", "14")
            )
            for rank, _ in hand_tup
        ]
    )
    if ranks == [2, 3, 4, 5, 14]:
        ranks = [1, 2, 3, 4, 5]
    count_n_rank = sorted(
        [(ranks.count(rank), rank) for rank in set(ranks)], reverse=True
    )
    counts, c_ranks = zip(*count_n_rank)
    flush, straight = False, False
    if len(set(suits)) == 1:
        flush = True
    if len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4:
        straight = True
    if flush and straight:
        return 8, c_ranks
    elif counts == (4, 1):
        return 7, c_ranks
    elif counts == (3, 2):
        return 6, c_ranks
    elif flush:
        return 5, c_ranks
    elif straight:
        return 4, c_ranks
    elif 3 in counts:
        return 3, c_ranks
    elif counts == (2, 2, 1):
        return 2, c_ranks
    elif 2 in counts:
        return 1, c_ranks
    else:
        return 0, c_ranks
