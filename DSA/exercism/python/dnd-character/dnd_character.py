"""dnd_character.py

Implement A game of Dungeons & Dragons.
"""
import random


class Character:
    """Dungeons & Dragons Character"""

    def __init__(self):
        """
        set 6 abilities and hitpoints
        """
        self.strength = Character.play_dice()
        self.dexterity = Character.play_dice()
        self.constitution = Character.play_dice()
        self.intelligence = Character.play_dice()
        self.wisdom = Character.play_dice()
        self.charisma = Character.play_dice()

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        """ability
        return random choice 6 abilities
        """
        return random.choice(
            [
                self.strength,
                self.dexterity,
                self.constitution,
                self.intelligence,
                self.wisdom,
                self.charisma,
                self.hitpoints,
            ]
        )

    @classmethod
    def play_dice(cls) -> int:
        """
        get max 3 numbers of random 6 nums
        """
        dices = sorted([random.randint(1, 6) for _ in range(6)], reverse=True)
        return sum(dices[0:3])


def modifier(constitution: int) -> int:
    """modifier
    modifier character's constitution

    :param num: int
    :return: int
    """
    return (constitution - 10) // 2
