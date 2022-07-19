def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    l, r = int(input()), int(input())

    for num in arr[l : r + 1]:
        print(num)


if __name__ == "__main__":
    main()
