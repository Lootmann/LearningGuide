class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1

        return count


def main():
    sol = Solution()
    tests = [
        (14, 6),
        (8, 4),
        (123, 12),
    ]

    for test in tests:
        got = sol.numberOfSteps(test[0])
        want = test[1]
        assert got == want


if __name__ == "__main__":
    main()
