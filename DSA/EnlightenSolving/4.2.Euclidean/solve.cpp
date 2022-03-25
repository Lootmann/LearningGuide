#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int GCD(int m, int n) {
  if (n == 0) return m;
  return GCD(n, m % n);
}

int main() {
  FastIO;

  int m = 51, n = 15;
  cout << GCD(m, n) << '\n';
}
