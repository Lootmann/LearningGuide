from collections import defaultdict


class Graph:
    """Graph
    Directed Unweighted Graph
    """

    def __init__(self, length: int):
        self.graph = defaultdict(list)

        self.visits = [False] * length
        self.ins = [0] * length
        self.outs = [0] * length
        self._time = 1

    def add(self, vertex: int, neighbors: list):
        if len(neighbors) == 1:
            self.graph[vertex - 1] = []

        for nv in neighbors[1:]:
            self.graph[vertex - 1].append(nv - 1)

    def dfs(self, start: int):
        self.visits[start] = True
        self.ins[start] = self._time
        self._time += 1

        for nv in self.graph[start]:
            if self.is_visited(nv):
                continue

            self.visits[nv] = True
            self.dfs(nv)

        self.outs[start] = self._time
        self._time += 1

    def is_visited(self, vertex: int):
        return self.visits[vertex]

    def __str__(self) -> str:
        res = []
        for i in range(len(self.graph)):
            res.append(f"{i + 1} {self.ins[i]} {self.outs[i]}")
        return "\n".join(res)


def main():
    n = int(input())
    graph = Graph(n)

    for _ in range(n):
        line = list(map(int, input().split()))
        vertex = line[0]
        graph.add(vertex, line[1:])

    for start in range(n):
        if not graph.is_visited(start):
            graph.dfs(start)

    print(graph)


if __name__ == "__main__":
    main()
