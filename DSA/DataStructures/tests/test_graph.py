# tests/test_graph.py
from src.graph import UndirectedUnWeightedGraph


class TestGraph:
    def setup_method(self):
        """
        0 - 3 - 6
        |       |
        1 - 4 - 7
        |   |
        2   5 - 8
        """
        self.graph = UndirectedUnWeightedGraph()

        self.graph.add(0, 1)
        self.graph.add(0, 3)
        self.graph.add(1, 2)
        self.graph.add(1, 4)
        self.graph.add(3, 6)
        self.graph.add(4, 5)
        self.graph.add(4, 7)
        self.graph.add(5, 8)
        self.graph.add(6, 7)

    def test_graph_keys(self):
        assert self.graph.keys() == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def test_representation(self):
        test = """0: [1, 3]
            1: [0, 2, 4]
            2: [1]
            3: [0, 6]
            4: [1, 5, 7]
            5: [4, 8]
            6: [3, 7]
            7: [4, 6]
            8: [5]"""

        res = []

        for line in test.split("\n"):
            res.append(line.strip())

        assert str(self.graph) == "\n".join(res)

    def test_dfs_started_at_0(self):
        res = self.graph.dfs(0)
        assert res == "0 3 6 7 4 5 8 1 2"

    def test_dfs_started_at_4(self):
        res = self.graph.dfs(4)
        assert res == "4 7 6 3 0 1 2 5 8"

    def test_bfs_started_at_0(self):
        res = self.graph.bfs(0)
        assert res == "0 1 3 2 4 6 5 7 8"

    def test_bfs_started_at_4(self):
        res = self.graph.bfs(4)
        assert res == "4 1 5 7 0 2 8 6 3"
