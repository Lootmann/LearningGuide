#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n, "b")
        rev_bits = bits[::-1] + "0" * (32 - len(bits))

        return int(rev_bits, 2)


# @lc code=end
