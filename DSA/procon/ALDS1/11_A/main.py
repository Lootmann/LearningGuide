def main():
    n = int(input())
    r = range(n)
    graph = [[0 for _ in r] for _ in r]

    for _ in r:
        line = list(map(int, input().split()))
        vertex = line[0] - 1
        for nv in line[2:]:
            graph[vertex][nv - 1] = 1

    for row in graph:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
