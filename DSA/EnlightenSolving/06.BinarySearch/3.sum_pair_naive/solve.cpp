#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

int main() {
  FastIO;
  int n;
  cin >> n;

  vector<int> A(n), B(n);
  for (auto &a : A) cin >> a;
  for (auto &b : B) cin >> b;

  // sort(B.begin(), B.end());

  int k;
  cin >> k;

  int answer{0};
  for (auto a : A) {
    int pair_sum = 0;
    for (auto b : B) {
      pair_sum = a + b;

      if (pair_sum <= k) {
        answer = max(answer, pair_sum);
      }
    }
  }

  cout << answer << '\n';
}
