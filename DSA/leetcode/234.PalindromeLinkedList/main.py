from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []

        while head is not None:
            lst.append(head.val)
            head = head.next

        return lst == lst[::-1]

    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        s = ""

        while head is not None:
            s += str(head.val)
            head = head.next

        return s == s[::-1]


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    sol = Solution()
    print(sol.isPalindrome(head))


if __name__ == "__main__":
    main()
