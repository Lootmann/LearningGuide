""" luhn.py

Given a number determine whether or not it is valid per the Luhn formula.
"""


class Luhn:
    def __init__(self, card_num: int):
        """
        convert num to reversed, white space stripped str
        """
        self.card_str = str(card_num).replace(" ", "").strip()[::-1]

    def valid(self) -> bool:
        """valid card_num

        Returns:
            bool: return True when self.card_str is luhn
        """
        if len(self.card_str) <= 1:
            return False

        # has any non-numbers
        for ch in self.card_str:
            if not ch.isnumeric():
                return False

        # calc
        size = len(self.card_str)
        total = 0

        for i in range(0, size, 2):
            total += int(self.card_str[i])

        for i in range(1, size, 2):
            num = int(self.card_str[i]) * 2
            if num > 9:
                num -= 9
            total += num

        return total % 10 == 0
