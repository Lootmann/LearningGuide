#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# @lc code=start


class Solution:
    def myAtoi(self, s: str) -> int:
        for ch in s:
            print(ch)

        if len(s) == 0:
            return 0

        if len(s) == 1:
            if s.isdigit():
                return int(s)
            return 0

        is_minus = False
        first_digit = False
        sign = False

        digits = []

        for i, ch in enumerate(s):
            print(i, ch)
            if first_digit and (not ch.isdigit()):
                break

            if sign and not ch.isdigit():
                return 0

            elif ch == " ":
                continue

            elif ch == "+":
                sign = True

            elif ch == "-":
                is_minus = True
                sign = True

            elif ch.isdigit():
                first_digit = True
                digits.append(ch)

            elif not ch.isdigit():
                if first_digit:
                    break
                else:
                    return 0

        print("dig: ", digits)
        concat = "".join(digits)
        num = int(concat)

        print("num: ", num)

        if is_minus:
            num *= -1

        if num < -(2**31):
            return -(2**31)

        if num > 2**31:
            return 2**31 - 1

        print("ans: ", num)

        return num


# @lc code=end
