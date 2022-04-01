#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int func(int n) {
  cout << "func(" << n << ")" << '\n';

  if (n == 0) return 0;

  int result = n + func(n - 1);
  cout << n << " " << result << '\n';

  return result;
}

int main() {
  FastIO;

  func(5);
}
