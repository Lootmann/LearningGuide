def main():
    n = int(input())

    memo = [0] * 45
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    print(memo[n])


if __name__ == "__main__":
    main()
