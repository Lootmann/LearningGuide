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

  vector<int> heights(n, 0);
  rep(i, n) cin >> heights[i];

  vector<int> dp(n, numeric_limits<int>::max());
  dp[0] = 0;

  for (std::size_t i = 1; i < heights.size(); ++i) {
    if (i == 1) {
      int diff1 = abs(heights.at(i) - heights.at(i - 1));
      dp[i] = diff1;
    } else {
      // dp: [i-1] [i]
      // dp[i-1] + abs(h[i] - h[i-1])
      int diff1 = abs(heights.at(i) - heights.at(i - 1)) + dp[i - 1];

      // dp: [i-2] [i-1] [i]
      // dp[i-2] + abs(h[i] - h[i-2])
      int diff2 = abs(heights.at(i) - heights.at(i - 2)) + dp[i - 2];

      // dp[i] = min(diff1, diff2);
      chmin(dp[i], min(diff1, diff2));
    }

    show(dp);
  }

  cout << dp[n - 1] << '\n';
}

int main() {
  FastIO;
  solve();
}
