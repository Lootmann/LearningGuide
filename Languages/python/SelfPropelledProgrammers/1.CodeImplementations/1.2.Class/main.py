"""
Class Design

1. When you expect taht a dict has specify key,
    it is better to define a "class".
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    last_name: str
    first_name: str
    birthday: date

    @property
    def fullname(self) -> str:
        return f"{self.last_name} {self.first_name}"

    @property
    def age(self) -> int:
        today = date.today()
        born = self.birthday
        elapsed = today.year - born.year

        if (today.month, today.day) < (born.month, born.day):
            return elapsed - 1
        return elapsed


def main():
    pass


if __name__ == "__main__":
    main()
