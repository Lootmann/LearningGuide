#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
  FastIO;

  int n, k;
  cin >> n >> k;

  vector<int> a(n);
  rep(i, n) cin >> a[i];

  bool exist = false;

  for (int bit = 0; bit < (1 << n); ++bit) {
    int sum = 0;
    for (int i = 0; i < n; ++i) {
      if (bit & (1 << i)) {
        sum += a[i];
      }
    }
    if (sum == k) exist = true;
  }

  cout << (exist ? "Yes" : "No") << "\n";
}
