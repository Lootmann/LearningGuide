#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: str) -> int:
        bits = format(n, "b")
        return bits.count("1")


# @lc code=end
