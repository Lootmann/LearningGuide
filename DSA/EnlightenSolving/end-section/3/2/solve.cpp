#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
  FastIO;

  int n, v;
  cin >> n >> v;

  vector<int> a(n);
  rep(i, n) cin >> a[i];

  int count = 0;
  for (int i = 0; i < n; ++i) {
    if (a[i] == v) {
      count++;
    }
  }
  cout << count << '\n';
}
