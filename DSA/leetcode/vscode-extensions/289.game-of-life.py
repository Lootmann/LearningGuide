#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
from typing import List


# @lc code=start
class Solution:
    def count_neighbor(self, board: List[List[int]], row: int, column: int) -> int:
        """
        count 1's numbers.
        horizontal, vertical, diagonal
        """
        cnt = 0
        row_limit = len(board)
        col_limit = len(board[0])

        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for x, y in zip(dx, dy):
            if 0 <= row + y < row_limit and 0 <= column + x < col_limit:
                if board[row + y][column + x] & 1:
                    cnt += 1

        return cnt

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_length = len(board)
        col_length = len(board[0])

        for r in range(row_length):
            for c in range(col_length):
                # current state
                current_state = board[r][c]

                # check neighbor counts
                neighbor_count = self.count_neighbor(board, r, c)

                if current_state == 1:
                    if neighbor_count in (2, 3):
                        board[r][c] |= 2

                if current_state == 0:
                    if neighbor_count == 3:
                        board[r][c] |= 2

        for i in range(row_length):
            for j in range(col_length):
                board[i][j] >>= 1

        return


# @lc code=end
