#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# @lc code=start


class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -(2**31), 2**31 - 1

        result = 0
        sign = 1
        seen = True

        for ch in s:
            # first char is allowed '+', '-' or digit
            if seen:
                if ch == " ":
                    continue
                elif ch == "-":
                    sign = -1
                elif ch.isdigit():
                    result = int(ch)
                elif ch != "+":
                    return 0
                seen = False

            # 2nd, 3rd, ... chars is only allowed 0-9 digit
            else:
                if ch.isdigit():
                    result = result * 10 + int(ch)
                    if sign * result < MIN:
                        return MIN
                    if sign * result > MAX:
                        return MAX

                else:
                    break

        return sign * result


# @lc code=end
