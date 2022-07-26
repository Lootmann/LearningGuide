def main():
    l1, r1, l2, r2 = map(int, input().split())

    points = [0] * 101

    for i in range(l1, r1 + 1):
        points[i] += 1

    for i in range(l2, r2 + 1):
        points[i] += 1

    ans = -1
    for point in points:
        if point == 2:
            ans += 1

    print(max(ans, 0))


if __name__ == "__main__":
    main()
