import string


class PhoneNumber:
    """
    The first three digits of the local number
        represent the *exchange code*,

    followed by the unique four-digit number
        which is the *subscriber number*.
    """

    def __init__(self, number: str):
        self._number = self.formatting(number)

    def formatting(self, number: str) -> str:
        self.area_code = ""
        self.exchange_code = ""
        self.subscriber_number = ""

        print("***" * 10)
        print(number)

        stripped = []
        for ch in number:
            if ch.isdigit():
                stripped.append(ch)
            elif ch in (" ", "-", ".", "(", ")", "+"):
                pass
            elif ch.isalpha():
                raise ValueError("letters not permitted")
            elif ch in list(string.punctuation):
                raise ValueError("punctuations not permitted")

        if len(stripped) > 11:
            raise ValueError("more than 11 digits")

        if len(stripped) < 10:
            raise ValueError("incorrect number of digits")

        if len(stripped) == 11 and stripped[0] != "1":
            raise ValueError("11 digits must start with 1")

        # delete country code
        if len(stripped) == 11 and stripped[0] == "1":
            stripped.pop(0)

        self.area_code = "".join(stripped[:3])
        self.exchange_code = "".join(stripped[3:6])
        self.subscriber_number = "".join(stripped[6:])

        print(self.area_code, self.exchange_code, self.subscriber_number)

        if self.area_code[0] == "0":
            raise ValueError("area code cannot start with zero")

        if self.area_code[0] == "1":
            raise ValueError("area code cannot start with one")

        if self.exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")

        if self.exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

        return "".join([self.area_code, self.exchange_code, self.subscriber_number])

    @property
    def number(self) -> str:
        return self._number

    def pretty(self) -> str:
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
