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
    int a, b;
    cin >> a >> b;
    G[a].emplace_back(b);
    // undirected graph
    G[b].emplace_back(a);
  }
}
