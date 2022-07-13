def is_prime(n: int) -> bool:
    if n in (2, 3):
        return True

    if n < 2 or 0 in (n % 2, n % 3):
        return False

    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def main():
    n = int(input())

    ans = 0
    for _ in range(n):
        num = int(input())
        if is_prime(num):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
