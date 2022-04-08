#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sign = 1
        if x < 0:
            x *= -1
            sign = -1

        ans = 0
        while x > 0:
            div, mod = divmod(x, 10)
            ans = ans * 10 + mod
            x = div

            # outbound
            if 2**31 < ans:
                return 0

        return sign * ans


# @lc code=end
