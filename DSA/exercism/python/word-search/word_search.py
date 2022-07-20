from typing import List, Optional, Tuple


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class WordSearch:
    def __init__(self, puzzle: List[str]):
        self.puzzle = puzzle

    def search(self, word: str) -> Optional[Tuple[Point, Point]]:
        width = len(self.puzzle[0])
        height = len(self.puzzle)
        word_len = len(word)

        # horizontal
        for row, line in enumerate(self.puzzle):
            idx = line.find(word)
            if idx != -1:
                return (Point(idx, row), Point(idx + word_len - 1, row))

            idx = line.find(word[::-1])
            if idx != -1:
                return (Point(idx + word_len - 1, row), Point(idx, row))

        # vertical
        for column in range(width):
            line = ""
            for row in range(height):
                line += self.puzzle[row][column]

            idx = line.find(word)
            if idx != -1:
                return (Point(column, idx), Point(column, idx + word_len - 1))

            idx = line.find(word[::-1])
            if idx != -1:
                return (Point(column, idx + word_len - 1), Point(column, idx))

        # diagonal

        # left-top right-bottom
        for row in range(height - word_len + 1):
            for col in range(width - word_len + 1):
                line = ""
                for i in range(word_len):
                    line += self.puzzle[row + i][col + i]

                if word == line:
                    return (
                        Point(row, col),
                        Point(row + word_len - 1, col + word_len - 1),
                    )

                if line == word[::-1]:
                    return (
                        Point(col + word_len - 1, row + word_len - 1),
                        Point(col, row),
                    )

        # right-top left-bottom
        for row in range(word_len, height):
            for col in range(width - word_len + 1):
                line = ""
                for i in range(word_len):
                    line += self.puzzle[row - i][col + i]

                if line == word:
                    return (
                        Point(row - word_len + 1, col + word_len - 1),
                        Point(row, col),
                    )

                if line == word[::-1]:
                    return (
                        Point(col + word_len - 1, row - word_len + 1),
                        Point(col, row),
                    )

        return None
