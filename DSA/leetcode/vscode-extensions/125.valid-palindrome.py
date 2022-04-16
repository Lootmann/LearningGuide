#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for ch in s.lower():
            if ch.isalnum():
                result.append(ch)

        return result == result[::-1]


# @lc code=end
