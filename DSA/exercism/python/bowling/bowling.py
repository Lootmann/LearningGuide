class BowlingGame:
    def __init__(self):
        self._score = 0
        self._frame_score = 0
        self._frame_index = 0

        self._is_spare = False
        self._is_strike = False

    def roll(self, pins: int) -> None:
        """
        all normal
        normal, spares
        normal, spares, strikes
        """
        if not 0 <= pins <= 10:
            raise ValueError("pins must be within 0 and 10")

        # first frame
        if self._frame_index % 2 == 0:
            self._frame_score = pins
        else:
            # second frame
            self._frame_score += pins
            self._score += self._frame_score
            self._frame_score = 0

        self._frame_index += 1
        self._is_spare = False
        self._is_strike = False

    def score(self) -> int:
        return self._score
