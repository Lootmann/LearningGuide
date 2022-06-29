# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self._direction = direction
        self._x_pos = x_pos
        self._y_pos = y_pos

    def move(self, movements: str) -> None:
        for m in movements:
            if m == "R":
                self._direction += 1

            if m == "L":
                self._direction += 3

            self._direction %= 4

            if m == "A":
                if self._direction == NORTH:
                    self._y_pos += 1
                if self._direction == EAST:
                    self._x_pos += 1
                if self._direction == SOUTH:
                    self._y_pos -= 1
                if self._direction == WEST:
                    self._x_pos -= 1

    @property
    def coordinates(self) -> tuple:
        return (self._x_pos, self._y_pos)

    @property
    def direction(self) -> int:
        return self._direction
