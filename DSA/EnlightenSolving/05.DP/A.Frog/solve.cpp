/*
 * https://atcoder.jp/contests/dp/tasks/dp_a
 */
#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;
using llint = long long int;

template <class T>
void chmin(T& a, T b) {
  if (a > b) a = b;
}

void solve() {
  int n;
  cin >> n;

  vector<llint> costs(n);
  for (auto& cost : costs) cin >> cost;

  vector<llint> dp(n, numeric_limits<llint>().max());
  dp[0] = 0;

  for (int i = 1; i < n; ++i) {
    chmin(dp[i], dp[i - 1] + abs(costs[i] - costs[i - 1]));
    if (i > 1) {
      chmin(dp[i], dp[i - 2] + abs(costs[i] - costs[i - 2]));
    }
  }

  cout << dp[n - 1] << '\n';
}

int main() {
  FastIO;
  solve();
}
