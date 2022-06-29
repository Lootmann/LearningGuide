class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")

        if 7 < row:
            raise ValueError("row not on board")

        if column < 0:
            raise ValueError("column not positive")

        if 7 < column:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen: "Queen") -> bool:
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        for i in range(0, 8):
            # horizontal
            if i == another_queen.row and self.column == another_queen.column:
                return True

            # vertically
            if self.row == another_queen.row and i == another_queen.column:
                return True

        # diagnoal
        for i in range(-7, 8):
            # left-bottom to right-top
            row = self.row + i
            col = self.column + i

            if 0 <= row <= 7 and 0 <= col <= 7:
                if row == another_queen.row and col == another_queen.column:
                    return True

            # left-top to right-bottom
            row = self.row + i
            col = self.column - i

            if 0 <= row <= 7 and 0 <= col <= 7:
                if row == another_queen.row and col == another_queen.column:
                    return True

        return False
