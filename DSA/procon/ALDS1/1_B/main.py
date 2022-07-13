def divisors(a: int) -> set:
    s = set()

    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            s.add(i)
            s.add(a // i)
    return s


def main():
    x, y = map(int, input().split())

    x_set = divisors(x)
    y_set = divisors(y)

    ans = 1
    for num in x_set:
        if num in y_set:
            ans = max(ans, num)
    print(ans)


if __name__ == "__main__":
    main()
