#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

template <class T>
void chmin(T &a, const T b) {
  a = min(a, b);
}

auto show = [](auto v) {
  for (const auto &el : v) {
    cout << el << ' ';
  }
  cout << '\n';
};

void solve() {
  int n;
  cin >> n;

  vector<int> heights(n);
  for (auto &h : heights) cin >> h;

  vector<int> dp(n, numeric_limits<int>::max());
  dp[0] = 0;

  for (std::size_t i = 1; i < heights.size(); ++i) {
    chmin(dp[i], dp[i - 1] + abs(heights.at(i) - heights.at(i - 1)));
    if (i > 1) {
      chmin(dp[i], dp[i - 2] + abs(heights.at(i) - heights.at(i - 2)));
    }
  }
  show(dp);

  cout << dp[n - 1] << '\n';
}

int main() {
  FastIO;
  solve();
}
