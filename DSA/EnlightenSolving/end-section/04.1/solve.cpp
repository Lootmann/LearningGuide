#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

long long int tribo(long long int n) {
  if (n < 0) return 0;
  if (n == 0) return 0;
  if (n == 1) return 0;
  if (n == 2) return 1;
  return tribo(n - 1) + tribo(n - 2) + tribo(n - 3);
}

int main() {
  FastIO;

  vector<pair<int, int>> nums{
      make_pair(0, 0),  make_pair(1, 0),  make_pair(2, 1),   make_pair(3, 1),
      make_pair(4, 2),  make_pair(5, 4),  make_pair(6, 7),   make_pair(7, 13),
      make_pair(8, 24), make_pair(9, 44), make_pair(10, 81),
  };

  for (auto key : nums) {
    cout << tribo(key.first) << " " << key.second << '\n';
  }
}
