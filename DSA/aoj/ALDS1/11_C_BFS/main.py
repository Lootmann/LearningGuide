from collections import defaultdict, deque


class Graph:
    def __init__(self, length: int) -> None:
        self.graph = defaultdict(list)
        self.dists = [-1] * length

    def add(self, vertex: list):
        _from = vertex[0] - 1
        degree = vertex[1]

        if degree == 0:
            self.graph[_from] = []
        else:
            for nv in vertex[2:]:
                self.graph[_from].append(nv - 1)

    def bfs(self, start: int):
        que = deque()
        que.append(start)
        self.dists[0] = 0

        while que:
            vertex = que.popleft()
            dist = self.dists[vertex]

            for nv in self.graph[vertex]:
                if self.dists[nv] > -1:
                    continue

                self.dists[nv] = dist + 1
                que.append(nv)

    def __str__(self):
        res = []
        for i, _id in enumerate(self.dists):
            res.append(f"{i + 1} {_id}")
        return "\n".join(res)


def main():
    n = int(input())
    graph = Graph(n)

    for _ in range(n):
        line = list(map(int, input().split()))
        graph.add(line)

    graph.bfs(0)
    print(graph)


if __name__ == "__main__":
    main()
