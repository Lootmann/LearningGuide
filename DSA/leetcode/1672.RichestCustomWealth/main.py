from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for row in accounts:
            max_wealth = max(max_wealth, sum(row))
        return max_wealth

    def maximumWealth1(self, accounts: List[List[int]]) -> int:
        return max([sum(row) for row in accounts])


def main():
    tests = [
        ([[1, 2, 3], [3, 2, 1]], 6),
        ([[1, 5], [7, 3], [3, 5]], 10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
    ]

    for test in tests:
        sol = Solution()
        got = sol.maximumWealth(test[0])
        want = test[1]

        assert got == want


if __name__ == "__main__":
    main()
