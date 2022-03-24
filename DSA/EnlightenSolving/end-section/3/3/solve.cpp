#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define MAX 1000000;
using namespace std;

int main() {
  FastIO;

  int n;
  cin >> n;

  vector<int> a(n);
  rep(i, n) cin >> a[i];

  int lowest = MAX;
  int second = MAX;

  for (int i = 0; i < n; ++i) {
    if (lowest > a[i]) {
      second = lowest;
      lowest = a[i];
    } else if (second > a[i]) {
      second = a[i];
    }
  }

  cout << "lowest = " << lowest << '\n';
  cout << "second = " << second << '\n';
}
