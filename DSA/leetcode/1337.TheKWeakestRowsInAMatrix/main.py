from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst = []
        for i, row in enumerate(mat):
            lst.append((i, sum(row)))

        lst.sort(key=lambda x: x[1])
        ans = [val[0] for val in lst[:k]]

        return ans


def main():

    mat = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ]
    k = 2

    sol = Solution()
    print(sol.kWeakestRows(mat, k))


if __name__ == "__main__":
    main()
