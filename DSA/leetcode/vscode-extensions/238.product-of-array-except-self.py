#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(N) using division
        has_zero = False
        total = 1

        for num in nums:
            # when nums have 2 zeros, all elems are zero
            if num == 0 and has_zero:
                return [0] * len(nums)

            if num == 0:
                has_zero = True
            else:
                total *= num

        result = []

        if has_zero:
            for num in nums:
                if num == 0:
                    result.append(total)
                else:
                    result.append(0)

        else:
            for num in nums:
                result.append(total // num)

        return result


# @lc code=end
