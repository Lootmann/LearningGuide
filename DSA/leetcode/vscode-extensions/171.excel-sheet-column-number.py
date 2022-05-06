#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def charToInt(self, ch: str) -> int:
        """
        >>> charToInt("A")
        1
        >>> charToInt("Z")
        26
        """
        return ord(ch) - ord("A") + 1

    def titleToNumber(self, columnTitle: str) -> int:
        weight, total = 1, 0

        for ch in list(columnTitle)[::-1]:
            total += self.charToInt(ch) * weight
            weight *= 26

        return total


# @lc code=end
