#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        current_value = prices[0]

        for price in prices:
            current_value = min(current_value, price)
            max_value = max(max_value, price - current_value)

        return max_value


# @lc code=end
