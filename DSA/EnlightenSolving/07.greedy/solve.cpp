#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

void solve() {
  const vector<int> coins{500, 100, 50, 10, 5, 1};

  int X;
  cin >> X;

  vector<int> A(6);
  rep(i, 6) cin >> A[i];

  int result = 0;
  rep(i, 6) {
    // 大きい方から確認する
    int add = X / coins[i];

    if (add > A[i]) add = A[i];

    X -= coins[i] * add;
    result += add;
  }

  cout << result << '\n';
}

int main() {
  FastIO;
  int n;
  cin >> n;

  rep(i, n) {
    cout << "[TEST" << i + 1 << "]\n";
    solve();
  }
}
