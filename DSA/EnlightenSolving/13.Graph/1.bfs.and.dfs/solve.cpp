#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

using Graph = vector<vector<int>>;

void title(string msg) {
  cout << ">>> " << msg << "\n"s;
}

auto trace = [](auto graph, auto n) {
  title("trace");

  for (int i = 0; i < n; ++i) {
    cout << i << " {";
    for (auto cell : graph[i]) {
      cout << cell << ' ';
    }
    cout << "} \n";
  }
};

// Depth-First Search
void dfs(const Graph &G, int start) {
  title("Depth-First Search");

  int n = (int)G.size();
  vector<bool> seen(n, false);

  seen[start] = true;

  stack<int> todo;
  todo.push(start);

  while (!todo.empty()) {
    int v = todo.top();
    todo.pop();

    for (int nv : G[v]) {
      if (!seen[nv]) {
        seen[nv] = true;
        todo.push(nv);
      }
    }
  }  // while

  for (std::size_t i = 0; i < seen.size(); ++i) {
    cout << i << " " << seen[i] << '\n';
  }
}

// Breadth-First Search
void bfs(const Graph &G, int start) {
  title("Breadth-First Search");

  int n = (int)G.size();
  vector<bool> seen(n, false);

  seen[start] = true;

  queue<int> todo;
  todo.push(start);

  while (!todo.empty()) {
    int vector = todo.front();
    todo.pop();

    for (int nv : G[vector]) {
      if (!seen[nv]) {
        seen[nv] = true;
        todo.push(nv);
      }
    }
  }  // while

  for (int i = 0; i < n; ++i) {
    cout << i << " " << seen[i] << '\n';
  }
}

int main() {
  FastIO;

  int n, m;
  cin >> n >> m;

  Graph G(n);
  for (int i = 0; i < m; ++i) {
    int from, to;
    cin >> from >> to;

    // directed
    G[from].emplace_back(to);

    // undirected
    // G[to].emplace_back(from);
  }

  trace(G, n);

  // start from 0
  bfs(G, 0);
  dfs(G, 0);
}
