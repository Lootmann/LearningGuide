# src/graph.py
from src.queue import Queue


class UndirectedUnWeightedGraph:
    def __init__(self):
        self.graph = {}

    def add(self, _from, _to):
        if _from not in self.graph:
            self.graph[_from] = []

        if _to not in self.graph:
            self.graph[_to] = []

        self.graph[_from].append(_to)
        self.graph[_to].append(_from)

    def keys(self):
        return sorted(self.graph.keys())

    def dfs(self, start_vertex):
        orders = []
        visited = [False for _ in range(len(self.keys()))]
        stack = [start_vertex]

        while len(stack) != 0:
            vertex = stack.pop()

            if not visited[vertex]:
                orders.append(vertex)
                visited[vertex] = True

            # neighbor vertex
            for nv in self.graph[vertex]:
                if not visited[nv]:
                    stack.append(nv)

        return " ".join(map(str, orders))

    def bfs(self, start_vertex):
        orders = []
        visited = [False for _ in range(len(self.keys()))]
        que = Queue()
        que.enqueue(start_vertex)

        while not que.empty():
            vertex = que.dequeue().val

            if not visited[vertex]:
                orders.append(vertex)
                visited[vertex] = True

            for nv in self.graph[vertex]:
                if not visited[nv]:
                    que.enqueue(nv)

        return " ".join(map(str, orders))

    def __str__(self) -> str:
        res = []
        for key in self.keys():
            res.append(f"{key}: {self.graph[key]}")
        return "\n".join(res)
