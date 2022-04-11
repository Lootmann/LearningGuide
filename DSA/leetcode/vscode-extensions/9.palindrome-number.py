#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        if len(s) == 1:
            return True

        return s == s[::-1]


# @lc code=end
