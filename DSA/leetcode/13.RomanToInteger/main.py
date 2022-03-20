class Solution:
    symbol_to_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        lst = [self.symbol_to_value[ch] for ch in list(s)]
        total = 0

        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                total -= lst[i]
            else:
                total += lst[i]

        total += lst[-1]
        return total


def main():
    for i in range(4):
        print(f"[TEST {i}]")
        symbols = input()
        sol = Solution()

        result = sol.romanToInt(s=symbols)
        ans = int(input())

        print("result, ans = {}, {}\n".format(result, ans))


if __name__ == "__main__":
    main()
