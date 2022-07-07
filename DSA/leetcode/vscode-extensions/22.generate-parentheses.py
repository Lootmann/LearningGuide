#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from itertools import permutations
from typing import List


# @lc code=start
class Solution:
    def bfs(self, left: int, right: int, current: str, res: List[str]) -> List[str]:
        if left == 0 and right == 0:
            res.append(current)
            return

        if left > 0:
            self.bfs(left - 1, right, current + "(", res)

        if right > left:
            self.bfs(left, right - 1, current + ")", res)

        return res

    def generateParenthesis(self, n: int) -> List[str]:
        return self.bfs(n, n, "", [])


# @lc code=end
