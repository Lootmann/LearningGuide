#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

int lower_bound(vector<int> const &arr, int k) {
  int left = -1, right = (int)arr.size() - 1;

  while (right - left > 1) {
    int mid = left + (right - left) / 2;

    if (k <= arr[mid])
      right = mid;
    else
      left = mid;
  }

  return right;
}

int main() {
  FastIO;
  int n;
  cin >> n;

  vector<int> A(n), B(n);
  for (auto &a : A) cin >> a;
  for (auto &b : B) cin >> b;

  sort(A.begin(), A.end());
  sort(B.begin(), B.end());

  int k;
  cin >> k;

  int min_value = 20000000;
  for (auto a : A) {
    int result = lower_bound(B, k - a);
    min_value = min(min_value, a + B[result]);
  }

  cout << min_value << '\n';
}
