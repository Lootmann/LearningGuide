#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List


# @lc code=start
class Solution:
    def removeElement(reself, nums: List[int], val: int) -> int:
        cnt = 0
        for num in nums:
            if num == val:
                cnt += 1

        while cnt > 0:
            nums.remove(val)
            cnt -= 1

        print(nums)
        return len(nums)


# @lc code=end
