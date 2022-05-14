#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
from importlib.resources import path


class Solution:
    # TODO: use dp
    def uniquePaths(self, m: int, n: int) -> int:
        # memory O(n * m) -> max(O(n * m)) = 100000
        paths = [[0 for _ in range(n)] for _ in range(m)]

        # init column
        for column in range(n):
            paths[0][column] = 1

        # init row
        for row in range(m):
            paths[row][0] = 1

        # calc O(n * m)
        for i in range(m - 1):
            for j in range(n - 1):
                paths[i + 1][j + 1] = paths[i + 1][j] + paths[i][j + 1]

        return paths[m - 1][n - 1]


# @lc code=end
