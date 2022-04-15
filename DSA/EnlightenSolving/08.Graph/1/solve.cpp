#include <bits/stdc++.h>
using namespace std;

using Graph = vector<vector<int>>;

int main() {
  int n, m;
  cin >> n >> m;

  Graph graph(n);

  for (int i = 0; i < m; ++i) {
    int a, b;
    cin >> a >> b;

    // Undirected Graph
    graph[a].emplace_back(b);
    graph[b].emplace_back(a);
  }

  sort(graph.begin(), graph.end());

  for (auto row : graph) {
    for (auto cell : row) {
      cout << cell << ' ';
    }
    cout << '\n';
  }
}
