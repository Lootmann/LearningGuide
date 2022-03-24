// return Yes/No if given number is in array.
#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

int main() {
  FastIO;
  int n, v;
  cin >> n >> v;

  vector<int> a(n);

  // O(n)
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }

  // flag
  bool exist = false;

  // O(n)
  for (int i = 0; i < n; ++i) {
    if (a[i] == v) exist = true;
  }

  if (exist)
    cout << "Yes" << '\n';
  else
    cout << "No" << '\n';
}
