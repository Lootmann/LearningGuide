def total(basket: list) -> int:
    """total

    :param basket: list
    :return: int - sum of book cost
    """
    book_count = [0, 0, 0, 0, 0]

    for i in range(1, 6):
        book_count[i - 1] = basket.count(i)

    sets = [0] * max(book_count)

    for j in range(max(book_count)):
        for k in range(len(book_count)):
            if book_count[k] > 0:
                book_count[k] -= 1
                sets[j] += 1

    count_5 = 0
    count_3 = 0
    bill = 0

    prices = [800, 1520, 2160, 2560, 3000]

    for k in sets:
        if k == 5:
            count_5 += 1

        if k == 3:
            count_3 += 1

        bill += prices[k - 1]

    bill -= min(count_5, count_3) * 40

    return bill
