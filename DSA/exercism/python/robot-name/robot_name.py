""" Robot

Manage robot factory settings.
"""
from random import randint


class Robot:
    def __init__(self):
        self._name_pool = set()
        self._name = self.gen_name()

    @property
    def name(self) -> str:
        return self._name

    def gen_name(self) -> str:
        """gen_name

        name should have a following rule:

        [A-Z][A-Z][0-9][0-9][0-9]
        26*26*10*10*10 = 676000 patterns

        :param None:
        :return: str - robot name
        """
        while True:
            name = "{}{}{}{}{}".format(
                chr(ord("A") + randint(0, 25)),
                chr(ord("A") + randint(0, 25)),
                randint(0, 9),
                randint(0, 9),
                randint(0, 9),
            )

            if name not in self._name_pool:
                self._name_pool.add(name)
                return name

    def reset(self) -> None:
        self._name = self.gen_name()
