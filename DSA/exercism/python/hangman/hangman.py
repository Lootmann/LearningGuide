# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    selected: list

    def __init__(self, word: str):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

        self.answer = word
        self.selected = ["_"] * len(word)
        self.answer_set = set(word)

    def guess(self, char: str):
        # validation
        if self.get_status() == STATUS_WIN:
            raise ValueError("The game has already ended.")

        if self.remaining_guesses < 0:
            raise ValueError("The game has already ended.")

        if char in self.answer_set:
            self.answer_set.remove(char)
            for idx, ch in enumerate(self.answer):
                if ch == char:
                    self.selected[idx] = char
        else:
            self.remaining_guesses -= 1

        if len(self.answer_set) == 0:
            self.status = STATUS_WIN

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self) -> str:
        return "".join(self.selected)

    def get_status(self) -> str:
        return self.status
