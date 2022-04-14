#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

using Interval = pair<int, int>;

bool cmp(const Interval &a, const Interval &b) {
  return a.second < b.second;
}

void solve() {
  int n;
  cin >> n;

  vector<Interval> vals(n);
  rep(i, n) {
    cin >> vals[i].first >> vals[i].second;
  }

  // Interval.second DESC
  sort(vals.begin(), vals.end(), cmp);

  int res = 0;
  int current_end_time = 0;
  rep(i, n) {
    // |----|
    //    |-----|
    //        |---|
    if (vals[i].first < current_end_time) continue;

    ++res;
    current_end_time = vals[i].second;
  }

  cout << res << '\n';
}

int main() {
  FastIO;
  solve();
}
