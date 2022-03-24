#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define MAX 1000000;
#define MIN 0;
using namespace std;

int main() {
  FastIO;

  int n;
  cin >> n;

  vector<int> a(n);
  rep(i, n) cin >> a[i];

  int max = MIN;
  int min = MAX;

  for (int i = 0; i < n; ++i) {
    max = std::max(max, a[i]);
    min = std::min(min, a[i]);
  }

  cout << max - min << '\n';
}
