#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 10**5 + 1

        while head:
            if head.val >= 10**5 + 1:
                return True
            head.val = index
            index += 1
            head = head.next

        return False


# @lc code=end
