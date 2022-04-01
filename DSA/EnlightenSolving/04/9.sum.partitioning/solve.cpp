#include <bits/stdc++.h>
using namespace std;

bool func(int i, int w, const vector<int> &a) {
  if (i == 0) {
    return w == 0;
  }

  if (func(i - 1, w, a)) return true;
  if (func(i - 1, w - a[i - 1], a)) return true;

  return false;
}

int main() {
  int n;
  cin >> n;

  vector<int> a(n);
  for (auto &A : a) cin >> A;

  int tt;
  cin >> tt;

  for (int i = 0; i < tt; ++i) {
    int w;
    cin >> w;

    if (func(n, w, a))
      cout << "Yes" << '\n';
    else
      cout << "No" << '\n';
  }
}
