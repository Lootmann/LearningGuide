#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

void solve() {
  int n;
  cin >> n;

  vector<int> A(n), B(n), C(n);
  rep(i, n) cin >> A[i];
  rep(i, n) cin >> B[i];
  rep(i, n) cin >> C[i];

  sort(A.begin(), A.end());
  sort(C.begin(), C.end());

  long long ans = 0;
  for (auto b : B) {
    auto a = std::lower_bound(A.begin(), A.end(), b) - A.begin();
    auto c = std::upper_bound(C.begin(), C.end(), b) - C.begin();

    ans += a * (n - c);
  }

  cout << ans << '\n';
}

int main() {
  FastIO;
  solve();
}
