#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in {"(", "{", "["}:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                is_match = False
                popped = stack.pop()

                is_match |= popped == "(" and ch == ")"
                is_match |= popped == "{" and ch == "}"
                is_match |= popped == "[" and ch == "]"

                if not is_match:
                    return False

        return len(stack) == 0


# @lc code=end
