class ConnectGame:
    def __init__(self, board):
        self._board = []

        for line in board.split("\n"):
            self._board.append(list(line.replace(" ", "")))

        self.y_max = len(self._board)
        self.x_max = len(self._board[0])

        cnt = 1
        for y in range(len(self._board)):
            for x in range(len(self._board[0])):
                # Do dfs when a mark is O or X
                if self._board[y][x] != ".":
                    self.dfs(y, x, self._board[y][x], cnt)
                    cnt += 1

    def dfs(self, x: int, y: int, mark: str, _id: int):
        """
          |-1| 0| 1|
        --+--+--+--+-
        -1| x| o| o|
        --+--+--+--+
         0| o| x| o|
        --+--+--+--+
         1| o| o| x|

        left-top and right-bot diagonal moves are not allowed.
        visited marks are "Xnn" or "Onn", nn = [1-9][0-9]{n}
        """
        dx = [-1, -1, 0, 0, 1, 1]
        dy = [0, 1, -1, 1, -1, 0]

        for (y_i, x_i) in zip(dy, dx):
            yy, xx = y + y_i, x + x_i
            if 0 <= yy < self.y_max and 0 <= xx < self.x_max:
                if self._board[yy][xx] == mark:
                    self._board[yy][xx] = mark + str(_id)
                    self.dfs(xx, yy, mark, _id)

    def get_winner(self) -> str:
        if len(self._board) == 1:
            return self._board[0][0]

        top = self._board[0]
        bot = self._board[-1]
        length = len(self._board)
        left = [self._board[i][-1] for i in range(length)]
        right = [self._board[i][0] for i in range(length)]

        # top, bot
        for a in top:
            if a != "." and len(a) >= 2:
                if a in bot:
                    return a[0]

        # left, right
        for a in left:
            if a != "." and len(a) >= 2:
                if a in right:
                    return a[0]

        return ""
