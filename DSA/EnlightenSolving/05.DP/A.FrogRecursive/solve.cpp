#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;
using llint = long long int;

const llint MAX = numeric_limits<llint>().max();

vector<llint> dp;

template <class T>
void chmin(T& a, T b) {
  if (a > b) a = b;
}

llint rec(int i, const vector<llint>& height) {
  // cached
  if (dp[i] < MAX) return dp[i];

  // base case
  if (i == 0) return 0;

  llint res = MAX;
  chmin(res, rec(i - 1, height) + abs(height[i] - height[i - 1]));
  if (i > 1) chmin(res, rec(i - 2, height) + abs(height[i] - height[i - 2]));

  // memorization
  return dp[i] = res;
}

void solve() {
  int n;
  cin >> n;

  vector<llint> h(n);
  for (auto& c : h) cin >> c;

  dp.assign(n, MAX);
  cout << rec(n - 1, h) << '\n';
}

int main() {
  FastIO;
  solve();
}
