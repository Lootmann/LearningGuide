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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        result = ListNode(-1)
        answer = result
        advance = False

        while not (l1 is None and l2 is None and advance is False):
            current = 0

            if advance:
                current += 1
                advance = False

            if l1:
                current += l1.val
                l1 = l1.next

            if l2:
                current += l2.val
                l2 = l2.next

            if current >= 10:
                current -= 10
                advance = True

            if result.val == -1:
                result.val = current
            else:
                result.next = ListNode(current)
                result = result.next

        return answer


# @lc code=end
