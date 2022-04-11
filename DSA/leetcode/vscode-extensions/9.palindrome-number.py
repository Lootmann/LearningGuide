#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        # first digit must not be '0' as Zero
        if x < 0 or x % 10 == 0:
            return False

        num = 0
        tmp = x
        while tmp > 0:
            num = num * 10 + tmp % 10
            tmp //= 10

        return x == num


# @lc code=end
