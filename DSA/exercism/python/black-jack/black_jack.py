"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def is_facecard(card: str) -> bool:
    return card in ("J", "Q", "K")


def is_ace(card: str) -> bool:
    return card == "A"


def value_of_card(card) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if is_ace(card):
        return 1

    if is_facecard(card):
        return 10

    return int(card)


def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    number_one = value_of_card(card_one)
    number_two = value_of_card(card_two)

    if number_one == number_two:
        return (card_one, card_two)

    if number_one > number_two:
        return card_one

    return card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    def add_11_if_card_is_ace(value: int) -> int:
        if value == 1:
            return 11
        return value

    value_one = add_11_if_card_is_ace(value_of_card(card_one))
    value_two = add_11_if_card_is_ace(value_of_card(card_two))
    total = value_one + value_two

    if total < 11:
        return 11

    return 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    def is_10(card: str) -> bool:
        return card == "10"

    has_ace = is_ace(card_one) | is_ace(card_two)
    has_facecard = is_facecard(card_one) | is_facecard(card_two)
    has_10 = is_10(card_one) | is_10(card_two)

    return has_ace and (has_facecard or has_10)


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    number_one = value_of_card(card_one)
    number_two = value_of_card(card_two)
    return number_one == number_two


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total <= 11
