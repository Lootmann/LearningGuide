#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

from multiprocessing.connection import answer_challenge
from typing import Optional

from bs4 import ResultSet
from idna import valid_contextj


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sumList(lst: Optional[ListNode]) -> int:
        digit = 1
        total = 0
        while lst:
            total += lst.val * digit
            lst = lst.next
            digit *= 10
        return total

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        total = Solution.sumList(l1) + Solution.sumList(l2)
        answer = tmp = ListNode(0)

        if total == 0:
            return answer

        while total > 0:
            tmp.next = ListNode(total % 10)
            total //= 10
            tmp = tmp.next

        return answer.next


# @lc code=end
