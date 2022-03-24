#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

int main() {
  FastIO;

  int n, k;
  cin >> n >> k;

  vector<int> a(n), b(n);
  for (int i = 0; i < n; ++i) cin >> a[i];
  for (int i = 0; i < n; ++i) cin >> b[i];

  int min_value = INT_MAX;

  // O(N^2)
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      int total = a[i] + b[j];
      if (k <= total && total < min_value) {
        min_value = total;
      }
    }
  }

  cout << min_value << '\n';
}
