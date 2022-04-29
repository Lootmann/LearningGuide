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
        used = {n}

        while True:
            n = self.sum_of_digit(n)

            if n == 1:
                return True

            if n in used:
                return False

            used.add(n)


# @lc code=end
