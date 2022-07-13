from collections import defaultdict


class Graph:
    """
    Graph

    Undirected Unweighted Graph
    (v_i, v_j) == (v_j, v_i)
    """

    def __init__(self, num: int) -> None:
        self.visited = [-1] * num

        self.graph = defaultdict(list)
        for v in range(num):
            self.graph[v] = []

    def add(self, _from: int, _to: int):
        self.graph[_from].append(_to)
        self.graph[_to].append(_from)

    def dfs(self, start: int, _id: int):
        stack = [start]
        self.visited[start] = _id

        while len(stack) != 0:
            v = stack.pop()

            for nv in self.graph[v]:
                if not self.is_visisted(nv):
                    self.visited[nv] = _id
                    stack.append(nv)

    def is_visisted(self, vertex: int) -> bool:
        return self.visited[vertex] != -1

    def is_friend(self, _from: int, _to: int) -> bool:
        if self.visited[_from] == -1 or self.visited[_to] == -1:
            return False
        return self.visited[_from] == self.visited[_to]

    def __str__(self) -> str:
        res = []
        for k, v in self.graph.items():
            res.append(f"{k} {v}")
        return "\n".join(res)


def main():
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        _from, _to = map(int, input().split())
        graph.add(_from, _to)

    for i in range(n):
        if not graph.is_visisted(i):
            graph.dfs(i, i)

    q = int(input())
    for _ in range(q):
        _from, _to = map(int, input().split())
        if graph.is_friend(_from, _to):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
