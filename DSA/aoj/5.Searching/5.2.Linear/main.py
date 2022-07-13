import sys


def main():
    inputs = sys.stdin.readlines()

    s = list(map(int, inputs[1].strip().split()))
    t = list(map(int, inputs[3].strip().split()))

    cnt = 0

    for num in t:
        if num in s:
            cnt += 1

    sys.stdout.write(str(cnt))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
