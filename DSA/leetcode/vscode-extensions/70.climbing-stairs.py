#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        stairs = [0] * n

        stairs[0] = 1
        stairs[1] = 2

        for i in range(2, n):
            stairs[i] = stairs[i - 1] + stairs[i - 2]

        return stairs[-1]


# @lc code=end
