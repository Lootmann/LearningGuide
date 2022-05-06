#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # n = 3^x
        # log3_n = x
        if n <= 0:
            return False

        x = math.log(n, 3)
        return abs(x - round(x)) < 1e-10


# @lc code=end
