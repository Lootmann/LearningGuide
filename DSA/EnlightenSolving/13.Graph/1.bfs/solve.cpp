#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

using Graph = vector<vector<int>>;

int main() {
  FastIO;

  int n, m;
  cin >> n >> m;

  Graph G(n);
  for (int i = 0; i < m; ++i) {
    int from, to;
    cin >> from >> to;

    // undirected
    G[from].emplace_back(to);
    G[to].emplace_back(from);
  }

  for (int i = 0; i < n; ++i) {
    cout << i << " {";
    for (auto cell : G[i]) {
      cout << cell << ' ';
    }
    cout << "} \n";
  }
}
