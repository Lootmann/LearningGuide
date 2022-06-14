"""Solution to Ellen's Alien Game exercise."""
from typing import List, Tuple


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Alien gets hit by someone
        alien.health -= 1

        :param: None
        :return: None
        """
        self.health -= 1

    def is_alive(self) -> bool:
        """check Alien is alive

        :param: None
        :return: bool - return True when alien.health is greather than 0
        """
        return self.health > 0

    def teleport(self, x_coordinate: int, y_coordinate: int) -> None:
        """Alien teleports to (x, y)
        :param x_coordinate: int
        :param y_coordinate: int
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other: "Alien"):
        if (
            self.x_coordinate == other.x_coordinate
            and self.y_coordinate == other.y_coordinate
        ):
            print("Collision :^)")
        else:
            print("No Collision :^)")


def new_aliens_collection(pos: List[Tuple[int, int]]) -> List[Alien]:
    """new_aliens_collection
    this function below to call your Alien class with a list of coordinates.

    :param pos: List[Tuple[int, int]]
    :return: List[Alien]
    """
    aliens = []
    for (x_coordinate, y_coordinate) in pos:
        aliens.append(Alien(x_coordinate, y_coordinate))
    return aliens
