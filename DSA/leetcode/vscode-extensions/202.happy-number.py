#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def sum_of_digit(self, n) -> int:
        total = 0
        while n > 0:
            n, mod = divmod(n, 10)
            total += mod**2
        return total

    def isHappy(self, n: int) -> bool:
        used = set()

        while n not in used:
            used.add(n)
            n = self.sum_of_digit(n)

        return 1 in used


# @lc code=end
