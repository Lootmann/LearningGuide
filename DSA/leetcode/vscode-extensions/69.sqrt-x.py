#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int):
        ng = 0
        ok = x + 1

        # binary search
        while ok - ng > 1:
            mid = ng + (ok - ng) // 2

            if mid * mid <= x:
                ng = mid
            else:
                ok = mid

        return ng


# @lc code=end
