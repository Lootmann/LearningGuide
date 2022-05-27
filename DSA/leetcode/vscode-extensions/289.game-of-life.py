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
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for x, y in zip(dx, dy):
            if 0 <= row + y < len(board) and 0 <= column + x < len(board[0]):
                if board[row + y][column + x] == 1:
                    cnt += 1

        return cnt

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        next_gen = [[0] * len(board[0]) for _ in range(len(board))]

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                # current state
                current_state = cell

                # check neighbor counts
                neighbor_count = self.count_neighbor(board, r, c)

                if current_state == 1:
                    if neighbor_count < 2:
                        next_gen[r][c] = 0
                    if neighbor_count in (2, 3):
                        next_gen[r][c] = 1
                    if neighbor_count > 3:
                        next_gen[r][c] = 0

                if current_state == 0:
                    if neighbor_count == 3:
                        next_gen[r][c] = 1

        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                board[i][j] = next_gen[i][j]

        return


# @lc code=end
