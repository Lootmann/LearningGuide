#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int lower_bound(vector<int> const &arr, int key) {
  int left = -1, right = (int)arr.size() - 1;
  while (right - left > 1) {
    int mid = left + (right - left) / 2;
    if (key <= arr[mid])
      right = mid;
    else
      left = mid;
  }
  return right;
}

void solve() {
  int n;
  cin >> n;

  vector<int> A(n);
  for (auto &a : A) cin >> a;

  vector<int> B = A;
  sort(B.begin(), B.end());

  for (auto key : A) {
    int index = lower_bound(B, key);
    cout << index << '\n';
  }
}

int main() {
  FastIO;
  solve();
}
